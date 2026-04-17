#!/bin/bash
set -euo pipefail
file="/tmp/lpic101/lab01/answers/session.txt"
test -f "$file"
grep -qx "user=$(whoami)" "$file"
grep -qx "id=$(id)" "$file"
grep -qx "shell=$SHELL" "$file"
grep -q "^date=" "$file"
