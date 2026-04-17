# Tasks

1. Check whether `systemd` is the init system with `ps -p 1`.
2. Show the default target.
3. List active units.
4. Inspect the status of a common service such as `ssh`, `cron`, or `systemd-journald`.
5. Use `journalctl` to read recent logs.
6. Filter logs for a specific unit if one is available.
7. List failed units.
8. Enable or disable a service if the environment safely permits it.
9. Compare a target to the older SysV runlevel concept.
10. Note where service unit files are commonly stored.

## Helpful Commands

`ps -p 1`, `systemctl`, `journalctl`

## Challenge

Use `systemctl list-unit-files` to compare enabled, disabled, and static unit states.
