#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab04"
rm -rf "$root"
mkdir -p "$root/payload/docs" "$root/payload/logs"
printf 'release notes\n' > "$root/payload/docs/readme.txt"
printf 'alpha build\n' > "$root/payload/docs/build.txt"
printf 'log line 1\n' > "$root/payload/logs/app.log"
