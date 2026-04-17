#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab01"
rm -rf "$root"
mkdir -p "$root/answers" "$root/notes" "$root/bin" "$root/workspace/reports" "$root/workspace/scripts" "$root/archive"
printf 'welcome to lab 01\n' > "$root/notes/mission.txt"
cat > "$root/notes/onboarding-ticket.txt" <<'EOF'
Northwind Systems Onboarding Ticket
Owner: Linux Operations
Priority: High
Task: Validate shell basics before production access is granted.
EOF
printf '#!/bin/bash\necho health-check\n' > "$root/workspace/scripts/health-check.sh"
printf 'daily status\n' > "$root/workspace/reports/status.txt"
printf 'incident summary\n' > "$root/workspace/reports/incidents.txt"
chmod 644 "$root/workspace/scripts/health-check.sh"
