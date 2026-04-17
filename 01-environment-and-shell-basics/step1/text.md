# Mission Brief

Your team lead wants proof that you know exactly which account and shell you are using before you touch any company files.

## Lesson: Know Who You Are Before You Work

This is one of the most important early habits in Linux administration.

Before you edit files, restart services, or read protected data, you should always know:

- which user you are
- which groups you belong to
- which shell environment you are using
- what the current system time is

In a company environment, this is not just technical hygiene. It affects permissions, audit trails, shell startup behavior, and incident timelines.

### `whoami`

`whoami` prints the effective username of the current session.

Run:

```bash
whoami
```

Use it when you need the fastest possible confirmation of the account you are operating as.

### `id`

`id` gives a fuller identity report.

Run:

```bash
id
```

It typically shows:

- UID
- primary GID
- supplementary groups

This is especially useful when debugging permission issues.

### `echo $SHELL`

`echo $SHELL` prints the shell path stored in the `SHELL` environment variable.

Run:

```bash
echo $SHELL
```

This often shows your login shell, such as `/bin/bash` or `/bin/zsh`.

### `date`

`date` prints the current system date and time.

Run:

```bash
date
```

You will use this often for logs, timestamps, and incident reports.

## Company Task

1. Run `whoami` and confirm your current operator username.
2. Run `id` and inspect your UID, GID, and groups.
3. Run `echo $SHELL` to check your login shell.
4. Run `date` to capture the current system date and time.
5. Write the results into `/tmp/lpic101/lab01/answers/session.txt` using this format:

```text
user=<your-username>
id=<full-output-of-id>
shell=<your-shell-path>
date=<full-output-of-date>
```

## Why This Matters

You should always know your execution context before you make changes on a server. In a company environment, the wrong user or shell can mean the wrong permissions, wrong startup files, or wrong audit trail.
