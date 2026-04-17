#!/usr/bin/env python3
import json
import os
from pathlib import Path
from textwrap import dedent


ROOT = Path("/Users/manojkumar/Documents/lpic-101")


LABS = [
    {
        "dir": "01-environment-and-shell-basics",
        "title": "Lab 01: Environment and Shell Basics",
        "description": "Learn the shell as your control panel and prove you can orient yourself on a Linux host.",
        "story": "You have just joined the operations team. Before touching anything important, you need to confirm who you are, where you are, and how this shell behaves.",
        "workspace": "/tmp/lpic101/lab01",
        "setup": dedent(
            """\
            #!/bin/bash
            set -euo pipefail
            root="/tmp/lpic101/lab01"
            rm -rf "$root"
            mkdir -p "$root/answers" "$root/notes" "$root/bin"
            printf 'welcome to lab 01\\n' > "$root/notes/mission.txt"
            """
        ),
        "steps": [
            {
                "title": "Step 1: Identify Yourself",
                "text": dedent(
                    """\
                    # Mission Brief

                    The team lead wants a quick identity check before giving you access to anything sensitive.

                    ## Do This

                    1. Inspect your username with `whoami`.
                    2. Inspect your current shell with `echo $SHELL`.
                    3. Inspect your home directory with `echo $HOME`.
                    4. Write the results into `/tmp/lpic101/lab01/answers/session.txt` using this format:

                    ```text
                    user=<your-username>
                    shell=<your-shell-path>
                    home=<your-home-directory>
                    ```

                    ## Why This Matters

                    You should always know your execution context before you make changes on a server.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    file="/tmp/lpic101/lab01/answers/session.txt"
                    test -f "$file"
                    grep -qx "user=$(whoami)" "$file"
                    grep -qx "shell=$SHELL" "$file"
                    grep -qx "home=$HOME" "$file"
                    """
                ),
            },
            {
                "title": "Step 2: Navigate With Intent",
                "text": dedent(
                    """\
                    # Mission Brief

                    You now need to show that you can move around the filesystem without getting lost.

                    ## Do This

                    1. Change into `/tmp/lpic101/lab01`.
                    2. Create a hidden file named `.shell-basics`.
                    3. Create a directory named `notes/daily`.
                    4. Save the output of `pwd` into `/tmp/lpic101/lab01/notes/daily/current-path.txt`.
                    5. Use `ls -la` to confirm the hidden file is visible.

                    ## Teaching Cue

                    Hidden files begin with `.`. They are not special because of permissions, only because of naming.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    root="/tmp/lpic101/lab01"
                    test -f "$root/.shell-basics"
                    test -d "$root/notes/daily"
                    test -f "$root/notes/daily/current-path.txt"
                    grep -qx "$root" "$root/notes/daily/current-path.txt"
                    """
                ),
            },
            {
                "title": "Step 3: Ask Linux For Help",
                "text": dedent(
                    """\
                    # Mission Brief

                    Strong admins do not memorize everything. They know how to look things up quickly.

                    ## Do This

                    1. Open the manual for `ls` with `man ls`.
                    2. Run `whatis ls`.
                    3. Run `type cd`.
                    4. Save the output of `history | tail -n 5` into `/tmp/lpic101/lab01/answers/history-tail.txt`.
                    5. Create `/tmp/lpic101/lab01/answers/ready.txt` containing exactly:

                    ```text
                    LPIC-101 lab 01 ready
                    ```

                    ## Teaching Cue

                    `man`, `whatis`, and `type` answer different questions. Learn when to use each one.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    root="/tmp/lpic101/lab01"
                    test -s "$root/answers/history-tail.txt"
                    grep -qx "LPIC-101 lab 01 ready" "$root/answers/ready.txt"
                    """
                ),
            },
        ],
        "finish": "You built the habit of checking identity, navigation, and help before doing real work. That is the right instinct for every LPIC-101 lab that follows.",
    },
    {
        "dir": "02-files-and-directories",
        "title": "Lab 02: Files and Directories",
        "description": "Build and reorganize a small project tree while practicing creation, movement, and linking.",
        "story": "A teammate left behind a messy project folder. Your job is to organize it into something usable without losing anything important.",
        "workspace": "/tmp/lpic101/lab02",
        "setup": dedent(
            """\
            #!/bin/bash
            set -euo pipefail
            root="/tmp/lpic101/lab02"
            rm -rf "$root"
            mkdir -p "$root/inbox"
            printf 'draft 1\\n' > "$root/inbox/plan.txt"
            printf 'draft 2\\n' > "$root/inbox/todo.txt"
            printf 'draft 3\\n' > "$root/inbox/notes.txt"
            """
        ),
        "steps": [
            {
                "title": "Step 1: Build the Project Layout",
                "text": dedent(
                    """\
                    # Mission Brief

                    Start by creating a clean working structure.

                    ## Do This

                    1. Create `/tmp/lpic101/lab02/project` with subdirectories `docs`, `bin`, and `archive`.
                    2. Copy all files from `inbox/` into `project/docs/`.
                    3. Confirm the result with `find` or `ls -R`.

                    ## Teaching Cue

                    Create the directory structure first. Then move or copy data into the right place.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    root="/tmp/lpic101/lab02/project"
                    test -d "$root/docs"
                    test -d "$root/bin"
                    test -d "$root/archive"
                    test -f "$root/docs/plan.txt"
                    test -f "$root/docs/todo.txt"
                    test -f "$root/docs/notes.txt"
                    """
                ),
            },
            {
                "title": "Step 2: Move, Rename, and Link",
                "text": dedent(
                    """\
                    # Mission Brief

                    Now organize the files by purpose.

                    ## Do This

                    1. Move `todo.txt` from `project/docs/` to `project/bin/`.
                    2. Rename `plan.txt` to `project-plan.txt` inside `project/docs/`.
                    3. Create a hard link named `project/archive/project-plan.hard`.
                    4. Create a symbolic link named `project/archive/current-notes.link` pointing to `project/docs/notes.txt`.

                    ## Teaching Cue

                    A hard link shares the inode. A symbolic link points to a path.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    root="/tmp/lpic101/lab02/project"
                    test -f "$root/bin/todo.txt"
                    test -f "$root/docs/project-plan.txt"
                    test -f "$root/archive/project-plan.hard"
                    test -L "$root/archive/current-notes.link"
                    inode_a=$(stat -c %i "$root/docs/project-plan.txt")
                    inode_b=$(stat -c %i "$root/archive/project-plan.hard")
                    test "$inode_a" = "$inode_b"
                    target=$(readlink "$root/archive/current-notes.link")
                    test "$target" = "$root/docs/notes.txt"
                    """
                ),
            },
            {
                "title": "Step 3: Inspect and Report",
                "text": dedent(
                    """\
                    # Mission Brief

                    Finish by documenting the structure you created.

                    ## Do This

                    1. Use `find` to list all regular files under `project/`.
                    2. Save that list to `/tmp/lpic101/lab02/report-files.txt`.
                    3. Use `stat` on `project/docs/project-plan.txt`.
                    4. Save the inode number only into `/tmp/lpic101/lab02/report-inode.txt`.

                    ## Teaching Cue

                    `find` answers structure questions. `stat` answers metadata questions.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    root="/tmp/lpic101/lab02"
                    test -s "$root/report-files.txt"
                    grep -q "project/docs/project-plan.txt" "$root/report-files.txt"
                    grep -q "project/bin/todo.txt" "$root/report-files.txt"
                    expected=$(stat -c %i "$root/project/docs/project-plan.txt")
                    grep -qx "$expected" "$root/report-inode.txt"
                    """
                ),
            },
        ],
        "finish": "You practiced the real file-management workflow: create, copy, move, rename, link, and inspect. That sequence turns messy data into a maintainable filesystem layout.",
    },
    {
        "dir": "03-text-processing-essentials",
        "title": "Lab 03: Text Processing Essentials",
        "description": "Extract value from structured text using the classic Unix toolchain.",
        "story": "You received a user inventory file and need to turn it into useful summaries for the team.",
        "workspace": "/tmp/lpic101/lab03",
        "setup": dedent(
            """\
            #!/bin/bash
            set -euo pipefail
            root="/tmp/lpic101/lab03"
            rm -rf "$root"
            mkdir -p "$root"
            cat > "$root/users.txt" <<'EOF'
            alice:x:1001:1001:Alice:/home/alice:/bin/bash
            bob:x:1002:1002:Bob:/home/bob:/bin/zsh
            carol:x:1003:1003:Carol:/home/carol:/bin/bash
            dave:x:1004:1004:Dave:/home/dave:/bin/sh
            alice:x:1001:1001:Alice:/home/alice:/bin/bash
            EOF
            """
        ),
        "steps": [
            {
                "title": "Step 1: Extract Usernames",
                "text": dedent(
                    """\
                    # Mission Brief

                    Start by pulling out just the usernames from the colon-separated file.

                    ## Do This

                    1. Use `cut` to extract field 1 from `/tmp/lpic101/lab03/users.txt`.
                    2. Sort the usernames.
                    3. Remove duplicates.
                    4. Save the final result to `/tmp/lpic101/lab03/usernames.txt`.

                    ## Teaching Cue

                    `cut`, `sort`, and `uniq` are small tools, but together they solve a lot of exam-style tasks.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    cat <<'EOF' > /tmp/lpic101/lab03/.expected
                    alice
                    bob
                    carol
                    dave
                    EOF
                    diff -u /tmp/lpic101/lab03/.expected /tmp/lpic101/lab03/usernames.txt
                    """
                ),
            },
            {
                "title": "Step 2: Filter for Bash Users",
                "text": dedent(
                    """\
                    # Mission Brief

                    The team lead only wants users who log in with Bash.

                    ## Do This

                    1. Use `grep` to select lines containing `/bin/bash`.
                    2. Save those lines into `/tmp/lpic101/lab03/bash-users.txt`.
                    3. Count the number of matching lines with `wc -l`.
                    4. Save only the number to `/tmp/lpic101/lab03/bash-count.txt`.

                    ## Teaching Cue

                    Save intermediate results when you are learning. It makes troubleshooting much easier.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    grep -q "^alice:" /tmp/lpic101/lab03/bash-users.txt
                    grep -q "^carol:" /tmp/lpic101/lab03/bash-users.txt
                    test "$(wc -l < /tmp/lpic101/lab03/bash-users.txt | tr -d ' ')" = "$(cat /tmp/lpic101/lab03/bash-count.txt | tr -d ' ')"
                    """
                ),
            },
            {
                "title": "Step 3: Transform the Delimiter",
                "text": dedent(
                    """\
                    # Mission Brief

                    Another tool expects comma-separated data instead of colon-separated data.

                    ## Do This

                    1. Replace `:` with `,` for the entire file.
                    2. Save the output to `/tmp/lpic101/lab03/users.csv`.
                    3. Use `tee` so you can see the output while also writing the file.

                    ## Teaching Cue

                    Delimiter conversion is a very common shell task, especially when exchanging data between tools.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    head -n 1 /tmp/lpic101/lab03/users.csv | grep -qx "alice,x,1001,1001,Alice,/home/alice,/bin/bash"
                    test "$(wc -l < /tmp/lpic101/lab03/users.csv | tr -d ' ')" = "5"
                    """
                ),
            },
        ],
        "finish": "You transformed raw text into targeted reports. That pipeline mindset is central to Linux administration and to LPIC-101 exam tasks.",
    },
    {
        "dir": "04-archive-and-compression",
        "title": "Lab 04: Archive and Compression",
        "description": "Pack, inspect, compress, and extract files the way admins do in daily Linux work.",
        "story": "A project directory needs to be archived before a handoff. You need to preserve structure and reduce size without losing visibility into the contents.",
        "workspace": "/tmp/lpic101/lab04",
        "setup": dedent(
            """\
            #!/bin/bash
            set -euo pipefail
            root="/tmp/lpic101/lab04"
            rm -rf "$root"
            mkdir -p "$root/payload/docs" "$root/payload/logs"
            printf 'release notes\\n' > "$root/payload/docs/readme.txt"
            printf 'alpha build\\n' > "$root/payload/docs/build.txt"
            printf 'log line 1\\n' > "$root/payload/logs/app.log"
            """
        ),
        "steps": [
            {
                "title": "Step 1: Create and Inspect a Tar Archive",
                "text": dedent(
                    """\
                    # Mission Brief

                    Package the project folder first without compression.

                    ## Do This

                    1. Create `/tmp/lpic101/lab04/payload.tar` from the `payload/` directory.
                    2. List the archive contents without extracting them.
                    3. Save that listing to `/tmp/lpic101/lab04/tar-list.txt`.

                    ## Teaching Cue

                    `tar` preserves the directory tree. Listing an archive before extraction is a useful safety habit.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    root="/tmp/lpic101/lab04"
                    test -f "$root/payload.tar"
                    tar -tf "$root/payload.tar" | grep -q "payload/docs/readme.txt"
                    grep -q "payload/logs/app.log" "$root/tar-list.txt"
                    """
                ),
            },
            {
                "title": "Step 2: Create a Compressed Archive",
                "text": dedent(
                    """\
                    # Mission Brief

                    The handoff channel is slow, so now compress the archive.

                    ## Do This

                    1. Create `/tmp/lpic101/lab04/payload.tar.gz`.
                    2. Compare the sizes of `payload.tar` and `payload.tar.gz`.
                    3. Save the size comparison from `ls -lh` into `/tmp/lpic101/lab04/size-report.txt`.

                    ## Teaching Cue

                    Archive first, compress second. That is why `.tar.gz` is such a common pattern.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    root="/tmp/lpic101/lab04"
                    test -f "$root/payload.tar.gz"
                    grep -q "payload.tar" "$root/size-report.txt"
                    grep -q "payload.tar.gz" "$root/size-report.txt"
                    """
                ),
            },
            {
                "title": "Step 3: Extract and Confirm",
                "text": dedent(
                    """\
                    # Mission Brief

                    The receiver wants proof that the archive restores cleanly.

                    ## Do This

                    1. Extract `payload.tar.gz` into `/tmp/lpic101/lab04/extracted/`.
                    2. Confirm that `readme.txt`, `build.txt`, and `app.log` were restored.
                    3. Save the extracted file listing into `/tmp/lpic101/lab04/extracted-list.txt`.

                    ## Teaching Cue

                    Successful extraction is part of the workflow. Backups that cannot be restored are not useful backups.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    root="/tmp/lpic101/lab04"
                    test -f "$root/extracted/payload/docs/readme.txt"
                    test -f "$root/extracted/payload/docs/build.txt"
                    test -f "$root/extracted/payload/logs/app.log"
                    grep -q "extracted/payload/docs/readme.txt" "$root/extracted-list.txt"
                    """
                ),
            },
        ],
        "finish": "You practiced the full archive lifecycle: create, inspect, compress, and restore. That is the pattern worth remembering, not just the flags.",
    },
    {
        "dir": "05-file-permissions-and-ownership",
        "title": "Lab 05: File Permissions and Ownership",
        "description": "Make access behavior deliberate by setting modes on files and directories.",
        "story": "Your team needs a shared project area, but different files should allow different levels of access.",
        "workspace": "/tmp/lpic101/lab05",
        "setup": dedent(
            """\
            #!/bin/bash
            set -euo pipefail
            root="/tmp/lpic101/lab05"
            rm -rf "$root"
            mkdir -p "$root/team"
            printf '#!/bin/bash\\necho deploy\\n' > "$root/team/deploy.sh"
            printf 'secret draft\\n' > "$root/team/secret.txt"
            chmod 644 "$root/team/deploy.sh" "$root/team/secret.txt"
            """
        ),
        "steps": [
            {
                "title": "Step 1: Protect a Sensitive File",
                "text": dedent(
                    """\
                    # Mission Brief

                    `secret.txt` must be readable by the owner, readable by the group, and inaccessible to everyone else.

                    ## Do This

                    1. Use `chmod` to set `/tmp/lpic101/lab05/team/secret.txt` to mode `640`.
                    2. Confirm the mode with `ls -l` or `stat`.

                    ## Teaching Cue

                    Learn to translate `rw-r-----` and `640` instantly. LPIC-101 expects that fluency.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    test "$(stat -c %a /tmp/lpic101/lab05/team/secret.txt)" = "640"
                    """
                ),
            },
            {
                "title": "Step 2: Make a Script Executable",
                "text": dedent(
                    """\
                    # Mission Brief

                    `deploy.sh` should be executable by the owner and group, but not writable by everyone.

                    ## Do This

                    1. Set `/tmp/lpic101/lab05/team/deploy.sh` to mode `750`.
                    2. Run the script directly to confirm execution works.

                    ## Teaching Cue

                    Execution requires the `x` bit. Reading a file and executing a file are not the same permission.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    file="/tmp/lpic101/lab05/team/deploy.sh"
                    test "$(stat -c %a "$file")" = "750"
                    test -x "$file"
                    """
                ),
            },
            {
                "title": "Step 3: Prepare a Shared Directory",
                "text": dedent(
                    """\
                    # Mission Brief

                    The team wants a shared directory where new files inherit the directory group.

                    ## Do This

                    1. Create `/tmp/lpic101/lab05/team/shared`.
                    2. Set its permissions to `2775`.
                    3. Confirm the setgid bit is present.

                    ## Teaching Cue

                    The setgid bit on directories is one of the most practical permission features for team workflows.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    dir="/tmp/lpic101/lab05/team/shared"
                    test -d "$dir"
                    test "$(stat -c %a "$dir")" = "2775"
                    """
                ),
            },
        ],
        "finish": "You moved beyond abstract permission theory and into realistic access patterns: private files, executable scripts, and shared directories.",
    },
    {
        "dir": "06-process-management",
        "title": "Lab 06: Process Management",
        "description": "Start, observe, stop, and persist processes with practical shell-based process control.",
        "story": "A lightweight service keeps appearing and disappearing on a test box. You need to prove you can manage its lifecycle intentionally.",
        "workspace": "/tmp/lpic101/lab06",
        "setup": dedent(
            """\
            #!/bin/bash
            set -euo pipefail
            root="/tmp/lpic101/lab06"
            rm -rf "$root"
            mkdir -p "$root/pids" "$root/logs"
            """
        ),
        "steps": [
            {
                "title": "Step 1: Launch and Record a Background Job",
                "text": dedent(
                    """\
                    # Mission Brief

                    Start a long-running process and make sure you can identify it again later.

                    ## Do This

                    1. Start `sleep 300` in the background.
                    2. Save its PID to `/tmp/lpic101/lab06/pids/sleep.pid`.
                    3. Use `ps` to inspect the PID you captured.

                    ## Teaching Cue

                    A PID file is a simple but useful way to keep track of a process you launched.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    pid=$(cat /tmp/lpic101/lab06/pids/sleep.pid)
                    ps -p "$pid" -o comm= | grep -qx "sleep"
                    """
                ),
            },
            {
                "title": "Step 2: Stop the Process Cleanly",
                "text": dedent(
                    """\
                    # Mission Brief

                    The test job is no longer needed. Shut it down and document what you stopped.

                    ## Do This

                    1. Terminate the PID saved in `/tmp/lpic101/lab06/pids/sleep.pid`.
                    2. Write the stopped PID into `/tmp/lpic101/lab06/logs/terminated.txt`.
                    3. Confirm with `ps` that the process is gone.

                    ## Teaching Cue

                    Good operators verify both the stop request and the actual stopped state.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    pid=$(cat /tmp/lpic101/lab06/pids/sleep.pid)
                    grep -qx "$pid" /tmp/lpic101/lab06/logs/terminated.txt
                    ! ps -p "$pid" > /dev/null
                    """
                ),
            },
            {
                "title": "Step 3: Keep a Job Running With Nohup",
                "text": dedent(
                    """\
                    # Mission Brief

                    Now launch a process that should survive after you close the current shell.

                    ## Do This

                    1. Start `sleep 120` with `nohup` in the background.
                    2. Redirect its output to `/tmp/lpic101/lab06/logs/nohup.out`.
                    3. Save its PID to `/tmp/lpic101/lab06/pids/nohup.pid`.

                    ## Teaching Cue

                    `nohup` is a simple way to decouple a process from the terminal session that started it.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    pid=$(cat /tmp/lpic101/lab06/pids/nohup.pid)
                    test -f /tmp/lpic101/lab06/logs/nohup.out
                    ps -p "$pid" -o comm= | grep -qx "sleep"
                    """
                ),
            },
        ],
        "finish": "You practiced the lifecycle of a process instead of just memorizing commands: launch, identify, stop, and keep alive when needed.",
    },
    {
        "dir": "07-package-management",
        "title": "Lab 07: Package Management",
        "description": "Learn how to inspect a system's package tooling and query the package database safely.",
        "story": "You are not allowed to make reckless package changes on a shared machine, but you still need to prove you understand the local package system.",
        "workspace": "/tmp/lpic101/lab07",
        "setup": dedent(
            """\
            #!/bin/bash
            set -euo pipefail
            root="/tmp/lpic101/lab07"
            rm -rf "$root"
            mkdir -p "$root/answers"
            """
        ),
        "steps": [
            {
                "title": "Step 1: Identify the Package Family",
                "text": dedent(
                    """\
                    # Mission Brief

                    Before using package tools, you must know what family the system belongs to.

                    ## Do This

                    1. Determine whether this environment uses Debian-style or RPM-style package tooling.
                    2. Save only one word into `/tmp/lpic101/lab07/answers/family.txt`:

                    ```text
                    debian
                    ```

                    or

                    ```text
                    rpm
                    ```

                    ## Teaching Cue

                    Do not start with installation commands. Start with identification.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    if command -v dpkg >/dev/null 2>&1; then
                      expected="debian"
                    elif command -v rpm >/dev/null 2>&1; then
                      expected="rpm"
                    else
                      echo "No supported package manager detected" >&2
                      exit 1
                    fi
                    grep -qx "$expected" /tmp/lpic101/lab07/answers/family.txt
                    """
                ),
            },
            {
                "title": "Step 2: Find the Package That Owns a File",
                "text": dedent(
                    """\
                    # Mission Brief

                    A teammate asks which package provided `/bin/ls`.

                    ## Do This

                    1. Use the appropriate package-query command for this distro family.
                    2. Save the raw answer into `/tmp/lpic101/lab07/answers/owner.txt`.

                    ## Teaching Cue

                    On Debian systems this is commonly `dpkg -S`. On RPM systems it is commonly `rpm -qf`.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    if command -v dpkg >/dev/null 2>&1; then
                      expected=$(dpkg -S /bin/ls)
                    else
                      expected=$(rpm -qf /bin/ls)
                    fi
                    diff -u <(printf '%s\n' "$expected") /tmp/lpic101/lab07/answers/owner.txt
                    """
                ),
            },
            {
                "title": "Step 3: Count Installed Packages",
                "text": dedent(
                    """\
                    # Mission Brief

                    Operations wants a quick inventory count from the package database.

                    ## Do This

                    1. Count the number of installed packages.
                    2. Save only the number to `/tmp/lpic101/lab07/answers/package-count.txt`.
                    3. Create `/tmp/lpic101/lab07/answers/tooling.txt` containing the exact command you used.

                    ## Teaching Cue

                    High-level package tools and low-level database tools serve different purposes. Learn both.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    if command -v dpkg-query >/dev/null 2>&1; then
                      expected=$(dpkg-query -W | wc -l | tr -d ' ')
                    else
                      expected=$(rpm -qa | wc -l | tr -d ' ')
                    fi
                    grep -qx "$expected" /tmp/lpic101/lab07/answers/package-count.txt
                    test -s /tmp/lpic101/lab07/answers/tooling.txt
                    """
                ),
            },
        ],
        "finish": "You stayed on the safe side of package management while still learning the most important instincts: identify the distro family and query the database correctly.",
    },
    {
        "dir": "08-boot-process-and-systemd",
        "title": "Lab 08: Boot Process and systemd",
        "description": "Inspect init, targets, and logs without assuming the environment behaves like a full VM.",
        "story": "You were asked to inspect service management on a Linux environment that might be a full host or a lightweight container. Your job is to observe, not assume.",
        "workspace": "/tmp/lpic101/lab08",
        "setup": dedent(
            """\
            #!/bin/bash
            set -euo pipefail
            root="/tmp/lpic101/lab08"
            rm -rf "$root"
            mkdir -p "$root/answers"
            """
        ),
        "steps": [
            {
                "title": "Step 1: Inspect PID 1",
                "text": dedent(
                    """\
                    # Mission Brief

                    The first question in any boot-related investigation is simple: what is PID 1 here?

                    ## Do This

                    1. Run `ps -p 1 -o comm=`.
                    2. Save the output to `/tmp/lpic101/lab08/answers/pid1.txt`.

                    ## Teaching Cue

                    In a container, PID 1 may not be `systemd`. That does not mean your commands are wrong. It means the environment is different.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    expected=$(ps -p 1 -o comm= | tr -d ' ')
                    actual=$(tr -d ' \n' < /tmp/lpic101/lab08/answers/pid1.txt)
                    test "$expected" = "$actual"
                    """
                ),
            },
            {
                "title": "Step 2: Check systemctl Availability",
                "text": dedent(
                    """\
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
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    file=/tmp/lpic101/lab08/answers/default-target.txt
                    if systemctl get-default >/dev/null 2>&1; then
                      expected=$(systemctl get-default)
                      grep -qx "$expected" "$file"
                    else
                      grep -qx "systemctl-unavailable" "$file"
                    fi
                    """
                ),
            },
            {
                "title": "Step 3: Capture Recent Logs",
                "text": dedent(
                    """\
                    # Mission Brief

                    Finish by collecting recent service or journal output.

                    ## Do This

                    1. Run `journalctl -n 5 --no-pager`.
                    2. If it works, save the output to `/tmp/lpic101/lab08/answers/journal.txt`.
                    3. If journal access is unavailable, save exactly `journalctl-unavailable` to that file.

                    ## Teaching Cue

                    Log access is one of the fastest ways to move from theory to diagnosis.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    file=/tmp/lpic101/lab08/answers/journal.txt
                    if journalctl -n 1 --no-pager >/dev/null 2>&1; then
                      test -s "$file"
                    else
                      grep -qx "journalctl-unavailable" "$file"
                    fi
                    """
                ),
            },
        ],
        "finish": "You learned the right investigative pattern: identify PID 1, test the service manager, and collect logs without assuming the environment behaves like a full booted server.",
    },
    {
        "dir": "09-hardware-and-system-architecture",
        "title": "Lab 09: Hardware and System Architecture",
        "description": "Turn Linux system information into a concise machine inventory.",
        "story": "Before installing software or planning storage, the team wants a quick inventory of the machine's kernel, architecture, memory, and block devices.",
        "workspace": "/tmp/lpic101/lab09",
        "setup": dedent(
            """\
            #!/bin/bash
            set -euo pipefail
            root="/tmp/lpic101/lab09"
            rm -rf "$root"
            mkdir -p "$root/answers"
            """
        ),
        "steps": [
            {
                "title": "Step 1: Capture Kernel and Architecture",
                "text": dedent(
                    """\
                    # Mission Brief

                    Start with the two fastest high-signal facts about the host.

                    ## Do This

                    1. Save the output of `uname -r` to `/tmp/lpic101/lab09/answers/kernel.txt`.
                    2. Save the output of `uname -m` to `/tmp/lpic101/lab09/answers/arch.txt`.

                    ## Teaching Cue

                    `uname` is often the quickest first glance at kernel and architecture state.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    grep -qx "$(uname -r)" /tmp/lpic101/lab09/answers/kernel.txt
                    grep -qx "$(uname -m)" /tmp/lpic101/lab09/answers/arch.txt
                    """
                ),
            },
            {
                "title": "Step 2: Measure Memory",
                "text": dedent(
                    """\
                    # Mission Brief

                    Operations wants the total installed memory recorded in a plain text file.

                    ## Do This

                    1. Determine the system's total memory from Linux tooling.
                    2. Save only the value from `/proc/meminfo` field `MemTotal` into `/tmp/lpic101/lab09/answers/memtotal.txt`.

                    ## Teaching Cue

                    Human-readable summaries are convenient, but raw values from `/proc` are precise and script-friendly.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    expected=$(awk '/MemTotal/ {print $2}' /proc/meminfo)
                    grep -qx "$expected" /tmp/lpic101/lab09/answers/memtotal.txt
                    """
                ),
            },
            {
                "title": "Step 3: Build a Device Inventory",
                "text": dedent(
                    """\
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
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    test -s /tmp/lpic101/lab09/answers/devices.txt
                    grep -qx "kernel=$(uname -r)" /tmp/lpic101/lab09/answers/summary.txt
                    grep -qx "arch=$(uname -m)" /tmp/lpic101/lab09/answers/summary.txt
                    grep -qx "memtotal=$(awk '/MemTotal/ {print $2}' /proc/meminfo)" /tmp/lpic101/lab09/answers/summary.txt
                    """
                ),
            },
        ],
        "finish": "You turned machine details into a usable inventory. That skill pays off every time you need to compare hosts or validate assumptions before making changes.",
    },
    {
        "dir": "10-partitions-and-filesystems",
        "title": "Lab 10: Partitions and Filesystems",
        "description": "Study real mount and filesystem information without taking unnecessary risks on the running system.",
        "story": "You are not provisioning new storage today, but you do need to read the system's storage layout like an administrator would.",
        "workspace": "/tmp/lpic101/lab10",
        "setup": dedent(
            """\
            #!/bin/bash
            set -euo pipefail
            root="/tmp/lpic101/lab10"
            rm -rf "$root"
            mkdir -p "$root/answers"
            """
        ),
        "steps": [
            {
                "title": "Step 1: Inspect Devices and Filesystems",
                "text": dedent(
                    """\
                    # Mission Brief

                    Start by looking at disks and known filesystems.

                    ## Do This

                    1. Run `lsblk -f`.
                    2. Save the output to `/tmp/lpic101/lab10/answers/lsblk-f.txt`.
                    3. Run `blkid` if available and append or save the output into `/tmp/lpic101/lab10/answers/blkid.txt`.

                    ## Teaching Cue

                    `lsblk -f` is usually the easiest overview. `blkid` is great when you care about labels and UUIDs.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    test -s /tmp/lpic101/lab10/answers/lsblk-f.txt
                    test -f /tmp/lpic101/lab10/answers/blkid.txt
                    """
                ),
            },
            {
                "title": "Step 2: Identify the Root Filesystem",
                "text": dedent(
                    """\
                    # Mission Brief

                    Determine what filesystem type backs the root mount.

                    ## Do This

                    1. Use `findmnt -n -o FSTYPE /` or another correct command.
                    2. Save only the root filesystem type to `/tmp/lpic101/lab10/answers/root-fstype.txt`.
                    3. Save the current mount entry for `/` to `/tmp/lpic101/lab10/answers/root-mount.txt`.

                    ## Teaching Cue

                    Reading the current mount state is a separate skill from editing future mount configuration.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    expected=$(findmnt -n -o FSTYPE /)
                    grep -qx "$expected" /tmp/lpic101/lab10/answers/root-fstype.txt
                    grep -q " / " /tmp/lpic101/lab10/answers/root-mount.txt || grep -q " /$" /tmp/lpic101/lab10/answers/root-mount.txt
                    """
                ),
            },
            {
                "title": "Step 3: Decode fstab",
                "text": dedent(
                    """\
                    # Mission Brief

                    Finish by demonstrating that you understand the six classic `fstab` fields.

                    ## Do This

                    1. Create `/tmp/lpic101/lab10/answers/fstab-fields.txt`.
                    2. Put these exact six lines into the file:

                    ```text
                    fs_spec
                    fs_file
                    fs_vfstype
                    fs_mntops
                    fs_freq
                    fs_passno
                    ```

                    ## Teaching Cue

                    Memorizing the field names is less important than understanding what each one controls, but the names are still worth knowing.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    cat <<'EOF' > /tmp/lpic101/lab10/.expected-fstab
                    fs_spec
                    fs_file
                    fs_vfstype
                    fs_mntops
                    fs_freq
                    fs_passno
                    EOF
                    diff -u /tmp/lpic101/lab10/.expected-fstab /tmp/lpic101/lab10/answers/fstab-fields.txt
                    """
                ),
            },
        ],
        "finish": "You practiced the safest and most important part of storage administration: reading the current state accurately before making changes.",
    },
    {
        "dir": "11-swap-and-filesystem-maintenance",
        "title": "Lab 11: Swap and Filesystem Maintenance",
        "description": "Investigate space, inodes, links, and swap like a troubleshooting Linux admin.",
        "story": "A host is reported as 'low on resources.' Your job is to inspect disk usage, link behavior, and swap state before anyone guesses at the cause.",
        "workspace": "/tmp/lpic101/lab11",
        "setup": dedent(
            """\
            #!/bin/bash
            set -euo pipefail
            root="/tmp/lpic101/lab11"
            rm -rf "$root"
            mkdir -p "$root/work" "$root/answers"
            printf 'disk check\\n' > "$root/work/source.txt"
            """
        ),
        "steps": [
            {
                "title": "Step 1: Inspect Capacity and Inodes",
                "text": dedent(
                    """\
                    # Mission Brief

                    First, determine whether the machine is short on bytes, inodes, or neither.

                    ## Do This

                    1. Save `df -h /` into `/tmp/lpic101/lab11/answers/root-capacity.txt`.
                    2. Save `df -i /` into `/tmp/lpic101/lab11/answers/root-inodes.txt`.

                    ## Teaching Cue

                    Disk full and inode full can look similar from the user's perspective, but they are different problems.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    grep -q "/" /tmp/lpic101/lab11/answers/root-capacity.txt
                    grep -q "/" /tmp/lpic101/lab11/answers/root-inodes.txt
                    """
                ),
            },
            {
                "title": "Step 2: Compare Hard and Symbolic Links",
                "text": dedent(
                    """\
                    # Mission Brief

                    Create both link types and compare their behavior.

                    ## Do This

                    1. Create a hard link at `/tmp/lpic101/lab11/work/source.hard`.
                    2. Create a symbolic link at `/tmp/lpic101/lab11/work/source.sym`.
                    3. Save the inode numbers of `source.txt` and `source.hard` into `/tmp/lpic101/lab11/answers/link-inodes.txt`.

                    ## Teaching Cue

                    If the inodes match, it is a hard link. If the path is separate, it is a symbolic link.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    root="/tmp/lpic101/lab11/work"
                    test -f "$root/source.hard"
                    test -L "$root/source.sym"
                    inode_a=$(stat -c %i "$root/source.txt")
                    inode_b=$(stat -c %i "$root/source.hard")
                    test "$inode_a" = "$inode_b"
                    grep -q "$inode_a" /tmp/lpic101/lab11/answers/link-inodes.txt
                    grep -q "$inode_b" /tmp/lpic101/lab11/answers/link-inodes.txt
                    """
                ),
            },
            {
                "title": "Step 3: Report Swap State",
                "text": dedent(
                    """\
                    # Mission Brief

                    Finish by checking whether swap is active on this machine.

                    ## Do This

                    1. Run `swapon --show`.
                    2. If it shows active swap, save the command output to `/tmp/lpic101/lab11/answers/swap.txt`.
                    3. If no swap is active, save exactly `no-swap-detected` to that file.

                    ## Teaching Cue

                    Not every environment uses swap, especially containers. Observation matters more than assumption.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    file=/tmp/lpic101/lab11/answers/swap.txt
                    if swapon --show | tail -n +2 | grep -q .; then
                      test -s "$file"
                    else
                      grep -qx "no-swap-detected" "$file"
                    fi
                    """
                ),
            },
        ],
        "finish": "You approached a maintenance problem the right way: inspect space, inspect inodes, compare links, and check swap before trying to fix anything.",
    },
    {
        "dir": "12-shell-scripting-basics",
        "title": "Lab 12: Shell Scripting Basics",
        "description": "Turn repetitive command sequences into a small, testable shell script.",
        "story": "You have repeated the same checks across many labs. Now it is time to package that behavior into a reusable script.",
        "workspace": "/tmp/lpic101/lab12",
        "setup": dedent(
            """\
            #!/bin/bash
            set -euo pipefail
            root="/tmp/lpic101/lab12"
            rm -rf "$root"
            mkdir -p "$root/sample" "$root/reports"
            printf 'alpha\\n' > "$root/sample/alpha.txt"
            printf 'beta\\n' > "$root/sample/beta.txt"
            """
        ),
        "steps": [
            {
                "title": "Step 1: Create a Script Skeleton",
                "text": dedent(
                    """\
                    # Mission Brief

                    Build the first version of your script.

                    ## Do This

                    1. Create `/tmp/lpic101/lab12/report.sh`.
                    2. Add a Bash shebang.
                    3. Make it executable.
                    4. Make the script print exactly these two lines when run with `hello` as the first argument:

                    ```text
                    mode=hello
                    today=<current-date-output-from-date +%F>
                    ```

                    ## Teaching Cue

                    Start small. A script that works in a tiny form is easier to grow safely.
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    script=/tmp/lpic101/lab12/report.sh
                    test -x "$script"
                    head -n 1 "$script" | grep -qx "#!/bin/bash"
                    expected_date=$(date +%F)
                    output=$("$script" hello)
                    printf '%s\n' "$output" | grep -qx "mode=hello"
                    printf '%s\n' "$output" | grep -qx "today=$expected_date"
                    """
                ),
            },
            {
                "title": "Step 2: Add a File Check",
                "text": dedent(
                    """\
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
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    script=/tmp/lpic101/lab12/report.sh
                    "$script" check /tmp/lpic101/lab12/sample/alpha.txt | grep -qx "file-exists=yes"
                    "$script" check /tmp/lpic101/lab12/sample/missing.txt | grep -qx "file-exists=no"
                    """
                ),
            },
            {
                "title": "Step 3: Add a Report Mode",
                "text": dedent(
                    """\
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
                    """
                ),
                "verify": dedent(
                    """\
                    #!/bin/bash
                    set -euo pipefail
                    report=/tmp/lpic101/lab12/reports/final-report.txt
                    test -s "$report"
                    grep -q "^hostname=" "$report"
                    grep -q "^files=2$" "$report"
                    grep -q "^item=alpha.txt$" "$report"
                    grep -q "^item=beta.txt$" "$report"
                    """
                ),
            },
        ],
        "finish": "You turned repeated shell work into a script with modes, conditionals, and a loop. That is a great final bridge from basic commands into automation.",
    },
]


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_executable(path: Path, content: str) -> None:
    write_file(path, content)
    os.chmod(path, 0o755)


for lab in LABS:
    lab_dir = ROOT / lab["dir"]
    intro = dedent(
        f"""\
        # {lab["title"]}

        ## Story Mode

        {lab["story"]}

        ## Workspace

        Use `{lab["workspace"]}` as your working area for this lab. The setup script prepares it for you.

        Move step by step. Each step has a verification check, so treat it like a guided practical rather than a worksheet.
        """
    )
    finish = dedent(
        f"""\
        # Lab Complete

        {lab["finish"]}

        ## Next Habit To Keep

        Before moving on, repeat the commands from memory once. Story mode works best when you combine guided practice with recall.
        """
    )

    details = {
        "intro": {
            "text": "intro.md",
            "background": "setup.sh",
        },
        "steps": [],
        "finish": {
            "text": "finish.md",
        },
    }

    for idx, step in enumerate(lab["steps"], start=1):
        step_dir = lab_dir / f"step{idx}"
        write_file(step_dir / "text.md", step["text"])
        write_executable(step_dir / "verify.sh", step["verify"])
        details["steps"].append(
            {
                "title": step["title"],
                "text": f"step{idx}/text.md",
                "verify": f"step{idx}/verify.sh",
            }
        )

    index = {
        "title": lab["title"],
        "description": lab["description"],
        "details": details,
        "backend": {
            "imageid": "ubuntu",
        },
    }

    write_file(lab_dir / "intro.md", intro)
    write_file(lab_dir / "finish.md", finish)
    write_executable(lab_dir / "setup.sh", lab["setup"])
    write_file(lab_dir / "index.json", json.dumps(index, indent=2))

    old_lab = lab_dir / "lab.md"
    if old_lab.exists():
        old_lab.unlink()
