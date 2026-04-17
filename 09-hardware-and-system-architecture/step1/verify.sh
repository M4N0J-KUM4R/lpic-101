#!/bin/bash
set -euo pipefail
grep -qx "$(uname -r)" /tmp/lpic101/lab09/answers/kernel.txt
grep -qx "$(uname -m)" /tmp/lpic101/lab09/answers/arch.txt
