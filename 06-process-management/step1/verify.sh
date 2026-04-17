#!/bin/bash
set -euo pipefail
pid=$(cat /tmp/lpic101/lab06/pids/sleep.pid)
ps -p "$pid" -o comm= | grep -qx "sleep"
