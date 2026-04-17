#!/bin/bash
set -euo pipefail
root="/tmp/lpic101/lab05"
rm -rf "$root"
mkdir -p "$root/team"
printf '#!/bin/bash\necho deploy\n' > "$root/team/deploy.sh"
printf 'secret draft\n' > "$root/team/secret.txt"
chmod 644 "$root/team/deploy.sh" "$root/team/secret.txt"
