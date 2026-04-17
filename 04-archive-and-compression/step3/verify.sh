#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab04"
test -f "$root/extracted/payload/docs/readme.txt"
test -f "$root/extracted/payload/docs/build.txt"
test -f "$root/extracted/payload/logs/app.log"
grep -q "extracted/payload/docs/readme.txt" "$root/extracted-list.txt"
