# Tasks

1. Display kernel name, release, and architecture.
2. Show CPU information.
3. Show memory statistics.
4. List block devices and their sizes.
5. Inspect loaded kernel modules.
6. Search the kernel ring buffer for device-related messages.
7. Display PCI or USB device information if the tools are available.
8. Determine whether the system is using 32-bit or 64-bit architecture.
9. Inspect `/proc/cpuinfo` and `/proc/meminfo`.
10. Summarize the hardware profile in a few lines.

## Helpful Commands

`uname`, `lscpu`, `free -h`, `lsblk`, `lsmod`, `dmesg`, `lspci`, `lsusb`, `cat /proc/cpuinfo`, `cat /proc/meminfo`

## Challenge

Use one command to print only the total installed memory in a human-readable format.
