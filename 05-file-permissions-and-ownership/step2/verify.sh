#!/bin/bash
set -euo pipefail
file="/tmp/lpic101/lab05/team/deploy.sh"
test "$(stat -c %a "$file")" = "750"
test -x "$file"
