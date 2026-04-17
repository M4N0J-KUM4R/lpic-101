#!/bin/bash
set -euo pipefail
test -s /tmp/lpic101/lab09/answers/devices.txt
grep -qx "kernel=$(uname -r)" /tmp/lpic101/lab09/answers/summary.txt
grep -qx "arch=$(uname -m)" /tmp/lpic101/lab09/answers/summary.txt
grep -qx "memtotal=$(awk '/MemTotal/ {print $2}' /proc/meminfo)" /tmp/lpic101/lab09/answers/summary.txt
