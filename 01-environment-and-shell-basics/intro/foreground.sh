#!/bin/bash
set -euo pipefail
echo "Preparing Northwind Systems onboarding workspace..."
while [ ! -f /tmp/lpic101/lab01/.intro-ready ]; do
  sleep 1
done
echo "Workspace ready."
