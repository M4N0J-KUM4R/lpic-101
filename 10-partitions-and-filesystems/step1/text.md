# Mission Brief

Start by looking at disks and known filesystems.

## Do This

1. Run `lsblk -f`.
2. Save the output to `/tmp/lpic101/lab10/answers/lsblk-f.txt`.
3. Run `blkid` if available and append or save the output into `/tmp/lpic101/lab10/answers/blkid.txt`.

## Teaching Cue

`lsblk -f` is usually the easiest overview. `blkid` is great when you care about labels and UUIDs.
