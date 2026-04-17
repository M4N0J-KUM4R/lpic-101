#!/bin/bash
set -euo pipefail
head -n 1 /tmp/lpic101/lab03/users.csv | grep -qx "alice,x,1001,1001,Alice,/home/alice,/bin/bash"
test "$(wc -l < /tmp/lpic101/lab03/users.csv | tr -d ' ')" = "5"
