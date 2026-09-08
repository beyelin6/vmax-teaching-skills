"""Run the canonical validator from a checkout or installed sync skill."""
import argparse
import json
from pathlib import Path
import runpy
import sys


def find_repository(explicit=None):
    here = Path(__file__).resolve()
    if explicit:
        candidates = [Path(explicit).expanduser().resolve()]
    else:
        candidates = list(here.parents)
        # Sync installs retain the selected cache path in their managed manifest.
        manifest = here.parents[2] / '.vmax-managed-skills.json'
        if manifest.is_file():
            data = json.loads(manifest.read_text(encoding='utf-8-sig'))
            if isinstance(data.get('cache_dir'), str):
                candidates.append(Path(data['cache_dir']))
    for candidate in candidates:
        script = candidate / 'scripts/validate_presentation.py'
        schema = candidate / 'core/schemas/vmax/render-request.schema.json'
        if script.is_file() and script.resolve() != here and schema.is_file():
            return script
    raise ValueError('Canonical repository not found. Use --repo-root with the full updated V-MAX checkout/cache path; do not use the course folder.')


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--repo-root')
    args, forwarded = parser.parse_known_args()
    try:
        script = find_repository(args.repo_root)
        sys.argv = [str(script), *forwarded]
        runpy.run_path(str(script), run_name='__main__')
    except (OSError, ValueError) as exc:
        print(f'VALIDATOR_SETUP_ERROR: {exc}', file=sys.stderr)
        return 2
    except ModuleNotFoundError as exc:
        print(f'VALIDATOR_DEPENDENCY_MISSING: {exc.name}. Install jsonschema>=4.18,<5 in this Python environment.', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
