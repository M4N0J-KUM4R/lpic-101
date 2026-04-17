# Tasks

1. Create a directory `/tmp/lpic101-perms` and a file inside it.
2. Inspect the current permissions in symbolic and numeric form.
3. Change the file mode with symbolic syntax, then again with octal syntax.
4. Set a restrictive umask and create a new file to observe the result.
5. Change the group ownership of a file if the environment allows it.
6. Change user ownership if the session is running with enough privileges.
7. Apply execute permission only to the owner.
8. Set the setgid bit on a directory and inspect the mode.
9. Remove write permission for group and others from a file.
10. Explain to yourself what `r`, `w`, and `x` mean for directories compared to files.

## Helpful Commands

`ls -l`, `stat`, `chmod`, `chown`, `chgrp`, `umask`

## Challenge

Create a file with exact mode `640` and confirm it with `stat` or `ls -l`.
