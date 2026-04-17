#!/bin/bash
set -euo pipefail
report=/tmp/lpic101/lab12/reports/final-report.txt
test -s "$report"
grep -q "^hostname=" "$report"
grep -q "^files=2$" "$report"
grep -q "^item=alpha.txt$" "$report"
grep -q "^item=beta.txt$" "$report"
