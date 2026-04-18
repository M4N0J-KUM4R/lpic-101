#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab01/answers"
diff -u <(type cd) "$root/type-cd.txt"
diff -u <(which ls) "$root/which-ls.txt"
test -s "$root/whatis-ls.txt"
grep -qx "man-ls-reviewed" "$root/man-done.txt"
