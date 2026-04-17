# Mission Brief

Create both link types and compare their behavior.

## Do This

1. Create a hard link at `/tmp/lpic101/lab11/work/source.hard`.
2. Create a symbolic link at `/tmp/lpic101/lab11/work/source.sym`.
3. Save the inode numbers of `source.txt` and `source.hard` into `/tmp/lpic101/lab11/answers/link-inodes.txt`.

## Teaching Cue

If the inodes match, it is a hard link. If the path is separate, it is a symbolic link.
