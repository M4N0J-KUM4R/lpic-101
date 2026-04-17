#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab11/work"
test -f "$root/source.hard"
test -L "$root/source.sym"
inode_a=$(stat -c %i "$root/source.txt")
inode_b=$(stat -c %i "$root/source.hard")
test "$inode_a" = "$inode_b"
grep -q "$inode_a" /tmp/lpic101/lab11/answers/link-inodes.txt
grep -q "$inode_b" /tmp/lpic101/lab11/answers/link-inodes.txt
