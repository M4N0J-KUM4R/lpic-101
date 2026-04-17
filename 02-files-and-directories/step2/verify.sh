#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab02/project"
test -f "$root/bin/todo.txt"
test -f "$root/docs/project-plan.txt"
test -f "$root/archive/project-plan.hard"
test -L "$root/archive/current-notes.link"
inode_a=$(stat -c %i "$root/docs/project-plan.txt")
inode_b=$(stat -c %i "$root/archive/project-plan.hard")
test "$inode_a" = "$inode_b"
target=$(readlink "$root/archive/current-notes.link")
test "$target" = "$root/docs/notes.txt"
