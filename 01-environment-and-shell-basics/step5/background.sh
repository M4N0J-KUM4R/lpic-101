#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab01"
rm -f "$root/answers/history-tail.txt" "$root/answers/handoff.txt"
touch "$root/.step5-ready"
