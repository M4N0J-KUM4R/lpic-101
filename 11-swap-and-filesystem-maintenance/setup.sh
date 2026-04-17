#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab11"
rm -rf "$root"
mkdir -p "$root/work" "$root/answers"
printf 'disk check\n' > "$root/work/source.txt"
