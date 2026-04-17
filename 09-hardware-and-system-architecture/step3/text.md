# Mission Brief

Finish with a basic block-device inventory for the machine.

## Do This

1. List block devices with `lsblk -dn -o NAME,SIZE`.
2. Save the output to `/tmp/lpic101/lab09/answers/devices.txt`.
3. Create `/tmp/lpic101/lab09/answers/summary.txt` with three lines using this format:

```text
kernel=<kernel-release>
arch=<architecture>
memtotal=<raw-memtotal-value>
```

## Teaching Cue

Good inventories mix raw data collection with short human-readable summaries.
