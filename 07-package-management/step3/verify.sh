#!/bin/bash
set -euo pipefail
if command -v dpkg-query >/dev/null 2>&1; then
  expected=$(dpkg-query -W | wc -l | tr -d ' ')
else
  expected=$(rpm -qa | wc -l | tr -d ' ')
fi
grep -qx "$expected" /tmp/lpic101/lab07/answers/package-count.txt
test -s /tmp/lpic101/lab07/answers/tooling.txt
