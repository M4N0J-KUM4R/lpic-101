#!/bin/bash
set -euo pipefail
echo "Preparing shift handoff review..."
while [ ! -f /tmp/lpic101/lab01/.step5-ready ]; do
  sleep 1
done
echo "Step 5 workspace is ready."
