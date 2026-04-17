#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab01"
test -f "$root/workspace/.operator-check"
grep -qx "$root/workspace" "$root/answers/workspace-path.txt"
test -s "$root/answers/workspace-ls.txt"
grep -q "reports" "$root/answers/workspace-ls.txt"
grep -q "scripts" "$root/answers/workspace-ls.txt"
grep -q "\.operator-check" "$root/answers/workspace-ls-la.txt"
