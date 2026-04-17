#!/bin/bash
set -euo pipefail
grep -q "^alice:" /tmp/lpic101/lab03/bash-users.txt
grep -q "^carol:" /tmp/lpic101/lab03/bash-users.txt
test "$(wc -l < /tmp/lpic101/lab03/bash-users.txt | tr -d ' ')" = "$(cat /tmp/lpic101/lab03/bash-count.txt | tr -d ' ')"
