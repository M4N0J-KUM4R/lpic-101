#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab01"
grep -qx "$root/workspace/reports" "$root/answers/reports-path.txt"
grep -qx "$root/workspace/scripts" "$root/answers/scripts-path.txt"
grep -qx "$root/workspace/reports" "$root/answers/backtrack-path.txt"
