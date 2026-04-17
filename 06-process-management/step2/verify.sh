#!/bin/bash
set -euo pipefail
pid=$(cat /tmp/lpic101/lab06/pids/sleep.pid)
grep -qx "$pid" /tmp/lpic101/lab06/logs/terminated.txt
! ps -p "$pid" > /dev/null
