                    #!/bin/bash
                    set -euo pipefail
                    script=/tmp/lpic101/lab12/report.sh
                    test -x "$script"
                    head -n 1 "$script" | grep -qx "#!/bin/bash"
                    expected_date=$(date +%F)
                    output=$("$script" hello)
                    printf '%s
' "$output" | grep -qx "mode=hello"
                    printf '%s
' "$output" | grep -qx "today=$expected_date"
