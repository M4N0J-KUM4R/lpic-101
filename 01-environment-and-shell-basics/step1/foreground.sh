#!/bin/bash
set -euo pipefail
echo "Checking operator identity packet..."
while [ ! -f /tmp/lpic101/lab01/.step1-ready ]; do
  sleep 1
done
echo "Step 1 workspace is ready."
