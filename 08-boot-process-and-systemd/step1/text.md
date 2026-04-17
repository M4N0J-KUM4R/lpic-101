# Mission Brief

The first question in any boot-related investigation is simple: what is PID 1 here?

## Do This

1. Run `ps -p 1 -o comm=`.
2. Save the output to `/tmp/lpic101/lab08/answers/pid1.txt`.

## Teaching Cue

In a container, PID 1 may not be `systemd`. That does not mean your commands are wrong. It means the environment is different.
