#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab02/project"
test -d "$root/docs"
test -d "$root/bin"
test -d "$root/archive"
test -f "$root/docs/plan.txt"
test -f "$root/docs/todo.txt"
test -f "$root/docs/notes.txt"
