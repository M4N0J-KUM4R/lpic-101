# Mission Brief

Finish by checking whether swap is active on this machine.

## Do This

1. Run `swapon --show`.
2. If it shows active swap, save the command output to `/tmp/lpic101/lab11/answers/swap.txt`.
3. If no swap is active, save exactly `no-swap-detected` to that file.

## Teaching Cue

Not every environment uses swap, especially containers. Observation matters more than assumption.
