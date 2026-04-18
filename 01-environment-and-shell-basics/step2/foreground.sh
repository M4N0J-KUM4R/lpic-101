#!/bin/bash
set -euo pipefail
echo "Refreshing support workspace for inspection..."
while [ ! -f /tmp/lpic101/lab01/.step2-ready ]; do
  sleep 1
done
echo "Step 2 workspace is ready."
