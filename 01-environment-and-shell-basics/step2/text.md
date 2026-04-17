# Mission Brief

The support team left a workspace for you. Before making changes, you need to inspect what is there and note hidden files too.

## Lesson 1: List Files

Welcome to your first real company task.

The operations team has prepared a workspace for you. Before you are allowed to edit anything, you must prove that you can inspect a directory correctly.

### What is `ls`?

`ls` is one of the first Linux commands every administrator learns.

It means: list directory contents.

When you run it, Linux shows the visible content of the current directory.

This is one of the core commands you will use on almost every Linux or Unix system.

### First Look at `ls`

1. Change into `/tmp/lpic101/lab01/workspace`.
2. Run `pwd` first so you know where you are.
3. Save the output of `pwd` to `/tmp/lpic101/lab01/answers/workspace-path.txt`.
4. Run `ls`.
5. Save the output of `ls` to `/tmp/lpic101/lab01/answers/workspace-ls.txt`.

At this point you should notice that `ls` gives you a simple directory view, but not much detail.

### What About Colors?

Many systems show colored output for `ls`. That color is a convenience feature added by shell configuration or aliases.

If you want to compare outputs, try:

```bash
ls --color=no
ls --color=yes
ls --color=auto .
```

You do not need to save those outputs for verification. This is just to help you observe that Linux can present the same command output in different visual styles.

### Get More Information With `ls -l`

Now the support lead wants more than just names. They want details.

Run:

```bash
ls -l .
```

This uses:

- `-l` for long listing format

The long listing usually shows:

- permissions
- hard link count
- owner
- group
- size
- modification date and time
- file name

### Show Hidden Files With `ls -la`

Some files are hidden because their names begin with a dot.

Now do the following:

1. Create a hidden file named `.operator-check`.
2. Run `ls -la`.
3. Save the output of `ls -la` to `/tmp/lpic101/lab01/answers/workspace-ls-la.txt`.

## Company Task Summary

Complete all of these:

1. Save the current workspace path.
2. Save the plain `ls` output.
3. Create the hidden file `.operator-check`.
4. Save the `ls -la` output that proves the hidden file is visible.

## Teaching Cue

`ls` gives you a quick visible listing.  
`ls -l` gives you details.  
`ls -la` gives you details plus hidden files.
