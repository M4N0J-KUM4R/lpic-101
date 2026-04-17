#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab02"
rm -rf "$root"
mkdir -p "$root/inbox"
printf 'draft 1\n' > "$root/inbox/plan.txt"
printf 'draft 2\n' > "$root/inbox/todo.txt"
printf 'draft 3\n' > "$root/inbox/notes.txt"
