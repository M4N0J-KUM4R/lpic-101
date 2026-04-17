#!/bin/bash
set -euo pipefail
file=/tmp/lpic101/lab11/answers/swap.txt
if swapon --show | tail -n +2 | grep -q .; then
  test -s "$file"
else
  grep -qx "no-swap-detected" "$file"
fi
