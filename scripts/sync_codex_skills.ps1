param(
    [string]$RepoUrl = "https://github.com/beyelin6/vmax-teaching-skills.git",
    [string]$Branch = "main",
    [string]$CodexSkillsDir = "$HOME\.codex\skills",
    [string]$CacheDir = "$HOME\.codex\vmax-teaching-skills-cache",
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$temporaryDryRunCache = $null

function Write-Step([string]$Message) {
    Write-Host "[V-MAX SYNC] $Message"
}

function Ensure-Git {
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        throw "git command not found. Install Git before running this sync script."
    }
}

function Read-SkillVersion([string]$SkillFile) {
    if (-not (Test-Path $SkillFile)) { return $null }
    $content = Get-Content -Raw -Encoding UTF8 $SkillFile
    $match = [regex]::Match($content, '(?m)^版本：\s*([^\r\n]+)')
    if ($match.Success) { return $match.Groups[1].Value.Trim() }
    $frontMatter = [regex]::Match($content, '(?ms)^---\s*(.*?)\s*---')
    if ($frontMatter.Success) {
        $versionMatch = [regex]::Match($frontMatter.Groups[1].Value, '(?m)^version:\s*["'']?([^\r\n"'']+)')
        if ($versionMatch.Success) { return $versionMatch.Groups[1].Value.Trim() }
    }
    return $null
}

Ensure-Git

$cacheParent = Split-Path -Parent $CacheDir
if (-not (Test-Path $cacheParent)) {
    if (-not $DryRun) { New-Item -ItemType Directory -Force -Path $cacheParent | Out-Null }
}

if (-not (Test-Path (Join-Path $CacheDir ".git"))) {
    Write-Step "Local cache not found; cloning repository."
    if (-not $DryRun) {
        git clone --depth 1 --branch $Branch $RepoUrl $CacheDir | Out-Host
    } else {
        $temporaryDryRunCache = Join-Path ([System.IO.Path]::GetTempPath()) ("vmax-dryrun-" + [guid]::NewGuid().ToString("N"))
        git clone --depth 1 --branch $Branch $RepoUrl $temporaryDryRunCache | Out-Host
        $CacheDir = $temporaryDryRunCache
    }
} else {
    Write-Step "Refreshing repository cache from GitHub."
    if (-not $DryRun) {
        git -C $CacheDir fetch origin $Branch --depth 1 | Out-Host
        git -C $CacheDir reset --hard "origin/$Branch" | Out-Host
        git -C $CacheDir clean -fd | Out-Host
    }
}

$sourceSkills = Join-Path $CacheDir "skills"
if (-not (Test-Path $sourceSkills)) {
    throw "Repository does not contain a skills directory: $sourceSkills"
}

if (-not (Test-Path $CodexSkillsDir)) {
    Write-Step "Creating Codex skills directory: $CodexSkillsDir"
    if (-not $DryRun) { New-Item -ItemType Directory -Force -Path $CodexSkillsDir | Out-Null }
}

$skillDirs = Get-ChildItem -Path $sourceSkills -Directory | Where-Object {
    Test-Path (Join-Path $_.FullName "SKILL.md")
} | Sort-Object Name

if (-not $skillDirs) {
    throw "No valid skills containing SKILL.md were found in $sourceSkills"
}

$managed = @()
foreach ($skill in $skillDirs) {
    $src = $skill.FullName
    $dst = Join-Path $CodexSkillsDir $skill.Name
    $version = Read-SkillVersion (Join-Path $src "SKILL.md")
    $action = if (Test-Path $dst) { "update" } else { "install" }

    $versionLabel = if ($version) { " v$version" } else { "" }
    Write-Step "$action $($skill.Name)$versionLabel"

    if (-not $DryRun) {
        $stage = Join-Path (Split-Path -Parent $dst) ("." + $skill.Name + ".sync-" + [guid]::NewGuid().ToString("N"))
        $backup = "$dst.previous"
        New-Item -ItemType Directory -Force -Path $stage | Out-Null
        robocopy $src $stage /MIR /R:2 /W:1 /NFL /NDL /NJH /NJS /NP | Out-Null
        $rc = $LASTEXITCODE
        if ($rc -ge 8) {
            Remove-Item -LiteralPath $stage -Recurse -Force -ErrorAction SilentlyContinue
            throw "robocopy failed for $($skill.Name) with exit code $rc"
        }
        if (Test-Path $backup) { Remove-Item -LiteralPath $backup -Recurse -Force }
        if (Test-Path $dst) { Move-Item -LiteralPath $dst -Destination $backup }
        try {
            Move-Item -LiteralPath $stage -Destination $dst
            if (Test-Path $backup) { Remove-Item -LiteralPath $backup -Recurse -Force }
        } catch {
            if (Test-Path $dst) { Remove-Item -LiteralPath $dst -Recurse -Force -ErrorAction SilentlyContinue }
            if (Test-Path $backup) { Move-Item -LiteralPath $backup -Destination $dst }
            throw
        }
    }

    $managed += [ordered]@{
        name = $skill.Name
        version = $version
        source = "skills/$($skill.Name)"
        destination = $dst
        action = $action
    }
}

$manifestPath = Join-Path $CodexSkillsDir ".vmax-managed-skills.json"
$report = [ordered]@{
    schema = "vmax-codex-skill-sync/1.0"
    repository = $RepoUrl
    branch = $Branch
    synced_at = (Get-Date).ToString("o")
    cache_dir = $CacheDir
    codex_skills_dir = $CodexSkillsDir
    skill_count = $managed.Count
    skills = $managed
    note = "Only V-MAX skill directories discovered from the repository are mirrored. Unrelated Codex skills are not touched."
}

if (-not $DryRun) {
    $report | ConvertTo-Json -Depth 6 | Set-Content -Path $manifestPath -Encoding UTF8
}

Write-Step "Completed. Discovered $($managed.Count) V-MAX skills."
Write-Step "Managed-skill manifest: $manifestPath"
$report | ConvertTo-Json -Depth 6

if ($temporaryDryRunCache -and (Test-Path $temporaryDryRunCache)) {
    Remove-Item -LiteralPath $temporaryDryRunCache -Recurse -Force -ErrorAction SilentlyContinue
}
