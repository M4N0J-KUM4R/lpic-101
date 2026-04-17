#!/bin/bash
set -euo pipefail
expected=$(findmnt -n -o FSTYPE /)
grep -qx "$expected" /tmp/lpic101/lab10/answers/root-fstype.txt
grep -q " / " /tmp/lpic101/lab10/answers/root-mount.txt || grep -q " /$" /tmp/lpic101/lab10/answers/root-mount.txt
