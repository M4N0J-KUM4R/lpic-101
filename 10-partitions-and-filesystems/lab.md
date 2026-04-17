# Tasks

1. List disks and partitions on the system.
2. Inspect filesystem types and UUIDs.
3. Review the current mount table.
4. Create a mount point under `/mnt/lpic101-demo`.
5. If a disposable device is available, create a filesystem on it.
6. Mount the filesystem manually.
7. Confirm the mount with `mount` or `findmnt`.
8. Unmount it safely.
9. Review `/etc/fstab` and identify each field.
10. Compare filesystem labels and UUID-based mounts.

## Helpful Commands

`lsblk -f`, `blkid`, `mount`, `umount`, `findmnt`, `fdisk`, `parted`, `mkfs`, `cat /etc/fstab`

## Challenge

Explain why UUIDs are usually preferred over device names like `/dev/sdb1` in `/etc/fstab`.
