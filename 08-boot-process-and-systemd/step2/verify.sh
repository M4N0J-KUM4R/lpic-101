#!/bin/bash
set -euo pipefail
file=/tmp/lpic101/lab08/answers/default-target.txt
if systemctl get-default >/dev/null 2>&1; then
  expected=$(systemctl get-default)
  grep -qx "$expected" "$file"
else
  grep -qx "systemctl-unavailable" "$file"
fi
