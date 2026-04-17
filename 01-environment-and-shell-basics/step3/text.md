# Mission Brief

The incident manager wants to know whether you can move between operational directories without losing context.

## Lesson: Move Through the Filesystem Deliberately

Now that you know who you are, the next skill is knowing where you are.

### `cd`

`cd` means change directory.

It changes the shell's current location.

Examples:

```bash
cd /tmp
cd ..
cd -
cd
```

Useful patterns:

- `cd /path`: go to an exact location
- `cd ..`: go one level up
- `cd -`: return to the previous directory
- `cd`: return to your home directory

### `pwd`

`pwd` means print working directory.

It tells you the exact directory your shell is currently using.

Run it often while learning:

```bash
pwd
```

### `clear`

`clear` clears the visible terminal screen.

It does not delete history. It just removes visual clutter so you can focus on your next task.

Run:

```bash
clear
```

## Company Task

1. Use `cd` to move into `/tmp/lpic101/lab01/workspace/reports`.
2. Run `pwd` and save the result to `/tmp/lpic101/lab01/answers/reports-path.txt`.
3. Use `cd ..` and then `cd scripts` to move into `/tmp/lpic101/lab01/workspace/scripts`.
4. Run `pwd` and save the result to `/tmp/lpic101/lab01/answers/scripts-path.txt`.
5. Use `cd -` to return to the previous directory.
6. Run `pwd` again and save the result to `/tmp/lpic101/lab01/answers/backtrack-path.txt`.
7. Run `clear` to clean up your terminal once you finish navigating.

## Teaching Cue

`cd` changes location.  
`pwd` confirms location.  
`clear` keeps your terminal readable while you work.
