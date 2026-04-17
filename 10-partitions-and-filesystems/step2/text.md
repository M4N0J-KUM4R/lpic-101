# Mission Brief

Determine what filesystem type backs the root mount.

## Do This

1. Use `findmnt -n -o FSTYPE /` or another correct command.
2. Save only the root filesystem type to `/tmp/lpic101/lab10/answers/root-fstype.txt`.
3. Save the current mount entry for `/` to `/tmp/lpic101/lab10/answers/root-mount.txt`.

## Teaching Cue

Reading the current mount state is a separate skill from editing future mount configuration.
