# Mission Brief

`deploy.sh` should be executable by the owner and group, but not writable by everyone.

## Do This

1. Set `/tmp/lpic101/lab05/team/deploy.sh` to mode `750`.
2. Run the script directly to confirm execution works.

## Teaching Cue

Execution requires the `x` bit. Reading a file and executing a file are not the same permission.
