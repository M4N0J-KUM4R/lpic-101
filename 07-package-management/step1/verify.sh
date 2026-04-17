#!/bin/bash
set -euo pipefail
if command -v dpkg >/dev/null 2>&1; then
  expected="debian"
elif command -v rpm >/dev/null 2>&1; then
  expected="rpm"
else
  echo "No supported package manager detected" >&2
  exit 1
fi
grep -qx "$expected" /tmp/lpic101/lab07/answers/family.txt
