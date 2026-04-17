#!/bin/bash
set -euo pipefail
pid=$(cat /tmp/lpic101/lab06/pids/nohup.pid)
test -f /tmp/lpic101/lab06/logs/nohup.out
ps -p "$pid" -o comm= | grep -qx "sleep"
