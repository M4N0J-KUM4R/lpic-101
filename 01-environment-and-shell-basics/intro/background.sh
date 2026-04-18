#!/bin/bash
set -euo pipefail
script_dir="$(cd "$(dirname "$0")/.." && pwd)"
bash "$script_dir/setup.sh"
touch /tmp/lpic101/lab01/.intro-ready
