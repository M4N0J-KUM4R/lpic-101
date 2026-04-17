#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab02"
test -s "$root/report-files.txt"
grep -q "project/docs/project-plan.txt" "$root/report-files.txt"
grep -q "project/bin/todo.txt" "$root/report-files.txt"
expected=$(stat -c %i "$root/project/docs/project-plan.txt")
grep -qx "$expected" "$root/report-inode.txt"
