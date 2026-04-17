# Mission Brief

The script should now accept a path and tell you whether it exists.

## Do This

1. Extend `report.sh` so `report.sh check /tmp/lpic101/lab12/sample/alpha.txt` prints:

```text
file-exists=yes
```

2. Make `report.sh check /tmp/lpic101/lab12/sample/missing.txt` print:

```text
file-exists=no
```

## Teaching Cue

This is your first useful conditional: respond differently based on filesystem state.
