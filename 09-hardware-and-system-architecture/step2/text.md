# Mission Brief

Operations wants the total installed memory recorded in a plain text file.

## Do This

1. Determine the system's total memory from Linux tooling.
2. Save only the value from `/proc/meminfo` field `MemTotal` into `/tmp/lpic101/lab09/answers/memtotal.txt`.

## Teaching Cue

Human-readable summaries are convenient, but raw values from `/proc` are precise and script-friendly.
