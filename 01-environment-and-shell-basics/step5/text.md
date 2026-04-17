# Mission Brief

Your shift is ending. Leave behind a short session handoff so the next junior operator can see what you checked today.

## Lesson: Review and Close Your Session

Professional terminal work includes a clean handoff.

### `history`

`history` shows commands you previously ran in the shell.

Run:

```bash
history
```

This helps you:

- repeat earlier commands
- review what you did
- create notes from a completed session

You can also filter it, for example:

```bash
history | tail -n 10
```

### `ls -la` for Final Review

Before handing work to someone else, check that the expected files exist.

This is another good use of `ls -la`: confirming files, hidden files, permissions, and timestamps in one view.

## Company Task

1. Run `history | tail -n 10` and save the output to `/tmp/lpic101/lab01/answers/history-tail.txt`.
2. Create `/tmp/lpic101/lab01/answers/handoff.txt` containing exactly:

```text
LPIC-101 lab 01 ready
```

3. Review the files in `/tmp/lpic101/lab01/answers` with `ls -la`.

## Teaching Cue

`history` helps you review your session.  
`ls -la` helps you confirm your handoff artifacts are actually there.
