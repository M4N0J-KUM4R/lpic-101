                    #!/bin/bash
                    set -euo pipefail
                    expected=$(ps -p 1 -o comm= | tr -d ' ')
                    actual=$(tr -d ' 
' < /tmp/lpic101/lab08/answers/pid1.txt)
                    test "$expected" = "$actual"
