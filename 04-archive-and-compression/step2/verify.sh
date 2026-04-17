#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab04"
test -f "$root/payload.tar.gz"
grep -q "payload.tar" "$root/size-report.txt"
grep -q "payload.tar.gz" "$root/size-report.txt"
