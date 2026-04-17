#!/bin/bash
set -euo pipefail
script=/tmp/lpic101/lab12/report.sh
"$script" check /tmp/lpic101/lab12/sample/alpha.txt | grep -qx "file-exists=yes"
"$script" check /tmp/lpic101/lab12/sample/missing.txt | grep -qx "file-exists=no"
