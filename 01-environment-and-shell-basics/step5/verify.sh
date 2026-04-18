#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab01/answers"
test -s "$root/history-tail.txt"
grep -qx "LPIC-101 lab 01 ready" "$root/handoff.txt"
