#!/bin/bash
set -euo pipefail
cat <<'EOF' > /tmp/lpic101/lab10/.expected-fstab
fs_spec
fs_file
fs_vfstype
fs_mntops
fs_freq
fs_passno
EOF
diff -u /tmp/lpic101/lab10/.expected-fstab /tmp/lpic101/lab10/answers/fstab-fields.txt
