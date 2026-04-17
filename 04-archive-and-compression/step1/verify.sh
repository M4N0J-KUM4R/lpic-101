#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab04"
test -f "$root/payload.tar"
tar -tf "$root/payload.tar" | grep -q "payload/docs/readme.txt"
grep -q "payload/logs/app.log" "$root/tar-list.txt"
