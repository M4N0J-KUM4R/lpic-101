# Mission Brief

Finish by adding a small report mode that loops over the sample directory.

## Do This

1. Extend `report.sh` so `report.sh report` prints:
2. One line starting with `hostname=`.
3. One line starting with `files=`.
4. One line for each file in `/tmp/lpic101/lab12/sample/` using the format `item=<filename>`.
5. Save the output of `report.sh report` to `/tmp/lpic101/lab12/reports/final-report.txt`.

## Teaching Cue

This step combines variables, conditionals, a `case`-style mode switch, and a loop into one small tool.
