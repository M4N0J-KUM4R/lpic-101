#!/bin/bash
set -euo pipefail
echo "Preparing navigation checkpoints..."
while [ ! -f /tmp/lpic101/lab01/.step3-ready ]; do
  sleep 1
done
echo "Step 3 workspace is ready."
