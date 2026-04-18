#!/bin/bash
set -euo pipefail
echo "Loading command research checkpoint..."
while [ ! -f /tmp/lpic101/lab01/.step4-ready ]; do
  sleep 1
done
echo "Step 4 workspace is ready."
