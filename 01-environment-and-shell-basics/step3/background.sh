#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab01"
rm -f "$root/answers/reports-path.txt" "$root/answers/scripts-path.txt" "$root/answers/backtrack-path.txt"
touch "$root/.step3-ready"
