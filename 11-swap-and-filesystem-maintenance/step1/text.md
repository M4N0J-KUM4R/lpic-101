# Mission Brief

First, determine whether the machine is short on bytes, inodes, or neither.

## Do This

1. Save `df -h /` into `/tmp/lpic101/lab11/answers/root-capacity.txt`.
2. Save `df -i /` into `/tmp/lpic101/lab11/answers/root-inodes.txt`.

## Teaching Cue

Disk full and inode full can look similar from the user's perspective, but they are different problems.
