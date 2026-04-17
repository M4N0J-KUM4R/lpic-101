# Mission Brief

Now launch a process that should survive after you close the current shell.

## Do This

1. Start `sleep 120` with `nohup` in the background.
2. Redirect its output to `/tmp/lpic101/lab06/logs/nohup.out`.
3. Save its PID to `/tmp/lpic101/lab06/pids/nohup.pid`.

## Teaching Cue

`nohup` is a simple way to decouple a process from the terminal session that started it.
