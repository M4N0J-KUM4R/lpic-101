# Tasks

1. Create a practice file at `/tmp/lpic101-users.txt` with at least 8 lines of colon-separated sample user data.
2. Display only the usernames using `cut`.
3. Sort the file by username.
4. Add some duplicate lines and use `sort | uniq` to remove duplicates.
5. Count total lines, words, and bytes with `wc`.
6. Search for a specific shell such as `/bin/bash` using `grep`.
7. Replace `:` with `,` using `tr` or another text utility.
8. Send output to both the terminal and a file with `tee`.
9. Redirect standard output to one file and standard error to another.
10. Use a pipeline of at least three commands to show only unique shells in sorted order.

## Helpful Commands

`cut`, `sort`, `uniq`, `wc`, `grep`, `tr`, `tee`, `head`, `tail`, `>`, `2>`

## Challenge

Use `grep -v` to print only the lines that do not contain `/bin/bash`.
