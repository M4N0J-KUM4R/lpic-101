# Mission Brief

Now organize the files by purpose.

## Do This

1. Move `todo.txt` from `project/docs/` to `project/bin/`.
2. Rename `plan.txt` to `project-plan.txt` inside `project/docs/`.
3. Create a hard link named `project/archive/project-plan.hard`.
4. Create a symbolic link named `project/archive/current-notes.link` pointing to `project/docs/notes.txt`.

## Teaching Cue

A hard link shares the inode. A symbolic link points to a path.
