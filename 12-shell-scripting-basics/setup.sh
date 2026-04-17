#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab12"
rm -rf "$root"
mkdir -p "$root/sample" "$root/reports"
printf 'alpha\n' > "$root/sample/alpha.txt"
printf 'beta\n' > "$root/sample/beta.txt"
