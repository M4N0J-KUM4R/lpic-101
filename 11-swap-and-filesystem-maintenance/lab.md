# Tasks

1. Check overall filesystem usage with `df -h`.
2. Inspect directory sizes under `/var` or `/tmp` with `du`.
3. Create a hard link and a symbolic link, then compare inode behavior.
4. Review active swap devices or files.
5. If safe in the environment, create a small swap file and prepare it with `mkswap`.
6. Enable and disable that swap file if privileges allow.
7. Inspect swap usage before and after activation.
8. Review how `fsck` is used and when it should not be run on a mounted writable filesystem.
9. Check inode usage with `df -i`.
10. Summarize the difference between capacity exhaustion and inode exhaustion.

## Helpful Commands

`df -h`, `df -i`, `du -sh`, `swapon --show`, `free -h`, `mkswap`, `swapon`, `swapoff`, `fsck`, `ln`

## Challenge

Find the five largest directories under `/var` using `du`, `sort`, and `head`.
