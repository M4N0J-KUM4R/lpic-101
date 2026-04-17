#!/bin/bash
set -euo pipefail
test "$(stat -c %a /tmp/lpic101/lab05/team/secret.txt)" = "640"
