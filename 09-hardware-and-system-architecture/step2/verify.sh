#!/bin/bash
set -euo pipefail
expected=$(awk '/MemTotal/ {print $2}' /proc/meminfo)
grep -qx "$expected" /tmp/lpic101/lab09/answers/memtotal.txt
