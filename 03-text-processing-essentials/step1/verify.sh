#!/bin/bash
set -euo pipefail
cat <<'EOF' > /tmp/lpic101/lab03/.expected
alice
bob
carol
dave
EOF
diff -u /tmp/lpic101/lab03/.expected /tmp/lpic101/lab03/usernames.txt
