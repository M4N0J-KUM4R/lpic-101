# Mission Brief

Start a long-running process and make sure you can identify it again later.

## Do This

1. Start `sleep 300` in the background.
2. Save its PID to `/tmp/lpic101/lab06/pids/sleep.pid`.
3. Use `ps` to inspect the PID you captured.

## Teaching Cue

A PID file is a simple but useful way to keep track of a process you launched.
