#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab01"
rm -f "$root/workspace/.operator-check"
rm -f "$root/answers/workspace-path.txt" "$root/answers/workspace-ls.txt" "$root/answers/workspace-ls-la.txt"
touch "$root/.step2-ready"
