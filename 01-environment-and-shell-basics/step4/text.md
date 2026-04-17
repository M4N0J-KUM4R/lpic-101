# Mission Brief

You are not expected to memorize every command. The operations team expects you to research unfamiliar tools properly before using them.

## Lesson: Learn Commands the Professional Way

Strong Linux operators do not guess. They inspect, verify, and read documentation.

This step introduces four tools that answer different questions.

### `type`

`type` tells you how the shell interprets a command name.

Run:

```bash
type cd
```

This is useful because some commands are:

- shell builtins
- aliases
- functions
- external executables

### `which`

`which` shows the executable path that will be used from your `PATH`.

Run:

```bash
which ls
```

This is most useful for commands that are real executables.

### `whatis`

`whatis` gives a one-line summary from the manual database.

Run:

```bash
whatis ls
```

This is a fast way to remind yourself what a command does.

### `man`

`man` opens the full manual page.

Run:

```bash
man ls
```

Inside `man`, remember:

- `q` quits
- `/text` searches
- `n` jumps to the next match

## Company Task

1. Run `type cd` and save the output to `/tmp/lpic101/lab01/answers/type-cd.txt`.
2. Run `which ls` and save the output to `/tmp/lpic101/lab01/answers/which-ls.txt`.
3. Run `whatis ls` and save the output to `/tmp/lpic101/lab01/answers/whatis-ls.txt`.
4. Open the manual page for `ls` with `man ls`.
5. Create `/tmp/lpic101/lab01/answers/man-done.txt` containing exactly:

```text
man-ls-reviewed
```

## Teaching Cue

`type` explains what a command is.  
`which` shows where an executable lives.  
`whatis` summarizes it quickly.  
`man` gives you the full reference.
