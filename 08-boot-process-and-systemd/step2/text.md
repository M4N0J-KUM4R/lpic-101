# Mission Brief

Next, determine whether `systemctl` can actually manage the current environment.

## Do This

1. Try `systemctl get-default`.
2. If it works, save the result to `/tmp/lpic101/lab08/answers/default-target.txt`.
3. If it does not work in this environment, create the same file containing exactly:

```text
systemctl-unavailable
```

## Teaching Cue

This is a great example of why environment awareness matters. LPIC-101 is about concepts, but real environments differ.
