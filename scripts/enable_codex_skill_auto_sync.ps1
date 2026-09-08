param(
    [string]$RepoRawBase = "https://raw.githubusercontent.com/beyelin6/vmax-teaching-skills/main",
    [string]$StartupName = "V-MAX-Codex-Skill-Sync.cmd",
    [switch]$Disable
)

$ErrorActionPreference = "Stop"

$startupDir = [Environment]::GetFolderPath("Startup")
if (-not $startupDir) {
    throw "Could not resolve the current user's Windows Startup folder."
}

$startupFile = Join-Path $startupDir $StartupName
$runnerDir = Join-Path $HOME ".codex\vmax-sync"
$runnerFile = Join-Path $runnerDir "run-vmax-skill-sync.ps1"

if ($Disable) {
    if (Test-Path $startupFile) { Remove-Item -Force $startupFile }
    Write-Host "[V-MAX AUTO SYNC] Disabled. Removed: $startupFile"
    exit 0
}

New-Item -ItemType Directory -Force -Path $runnerDir | Out-Null

$runner = @'
$ErrorActionPreference = "Stop"
$raw = "https://raw.githubusercontent.com/beyelin6/vmax-teaching-skills/main/scripts/sync_codex_skills.ps1"
$temp = Join-Path $env:TEMP "vmax-sync-codex-skills.ps1"
try {
    Invoke-WebRequest -UseBasicParsing -Uri $raw -OutFile $temp
    $powerShellHost = Get-Command pwsh.exe -ErrorAction SilentlyContinue
    if (-not $powerShellHost) { $powerShellHost = Get-Command powershell.exe -ErrorAction SilentlyContinue }
    if (-not $powerShellHost) { throw "No PowerShell host (pwsh.exe or powershell.exe) was found." }
    & $powerShellHost.Source -NoProfile -ExecutionPolicy Bypass -File $temp
} catch {
    $logDir = Join-Path $HOME ".codex\vmax-sync"
    New-Item -ItemType Directory -Force -Path $logDir | Out-Null
    $log = Join-Path $logDir "last-error.txt"
    "$(Get-Date -Format o) $($_.Exception.Message)" | Set-Content -Encoding UTF8 $log
    exit 1
}
'@

Set-Content -Path $runnerFile -Value $runner -Encoding UTF8

$powerShellHost = Get-Command pwsh.exe -ErrorAction SilentlyContinue
if (-not $powerShellHost) { $powerShellHost = Get-Command powershell.exe -ErrorAction SilentlyContinue }
if (-not $powerShellHost) { throw "No PowerShell host (pwsh.exe or powershell.exe) was found." }
$cmd = '@echo off' + "`r`n" + 'start "" /min "' + $powerShellHost.Source + '" -NoProfile -ExecutionPolicy Bypass -File "' + $runnerFile + '"' + "`r`n"
Set-Content -Path $startupFile -Value $cmd -Encoding ASCII

Write-Host "[V-MAX AUTO SYNC] Enabled for current user."
Write-Host "Startup entry: $startupFile"
Write-Host "Runner: $runnerFile"
Write-Host "At each Windows sign-in, V-MAX skills will be rediscovered and mirrored into $HOME\.codex\skills."
Write-Host "Unrelated Codex skills are not removed or modified."
