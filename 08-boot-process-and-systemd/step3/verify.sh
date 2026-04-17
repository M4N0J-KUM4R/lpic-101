#!/bin/bash
set -euo pipefail
file=/tmp/lpic101/lab08/answers/journal.txt
if journalctl -n 1 --no-pager >/dev/null 2>&1; then
  test -s "$file"
else
  grep -qx "journalctl-unavailable" "$file"
fi
