#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab03"
rm -rf "$root"
mkdir -p "$root"
cat > "$root/users.txt" <<'EOF'
alice:x:1001:1001:Alice:/home/alice:/bin/bash
bob:x:1002:1002:Bob:/home/bob:/bin/zsh
carol:x:1003:1003:Carol:/home/carol:/bin/bash
dave:x:1004:1004:Dave:/home/dave:/bin/sh
alice:x:1001:1001:Alice:/home/alice:/bin/bash
EOF
