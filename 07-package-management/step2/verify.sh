                    #!/bin/bash
                    set -euo pipefail
                    if command -v dpkg >/dev/null 2>&1; then
                      expected=$(dpkg -S /bin/ls)
                    else
                      expected=$(rpm -qf /bin/ls)
                    fi
                    diff -u <(printf '%s
' "$expected") /tmp/lpic101/lab07/answers/owner.txt
