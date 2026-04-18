#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab01"
rm -f "$root/answers/type-cd.txt" "$root/answers/which-ls.txt" "$root/answers/whatis-ls.txt" "$root/answers/man-done.txt"
touch "$root/.step4-ready"
