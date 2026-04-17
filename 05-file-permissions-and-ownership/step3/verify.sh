#!/bin/bash
set -euo pipefail
dir="/tmp/lpic101/lab05/team/shared"
test -d "$dir"
test "$(stat -c %a "$dir")" = "2775"
