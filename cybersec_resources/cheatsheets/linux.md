# Linux Command Line Cheat Sheet

## File Management
- `ls -la`: List all files with detailed information.
- `cp <source> <destination>`: Copy files or directories.
- `mv <source> <destination>`: Move or rename files.
- `rm -rf <file_or_directory>`: Remove files or directories.
- `find <directory> -name <filename>`: Search for a file.

## User Management
- `whoami`: Display the current user.
- `sudo adduser <username>`: Add a new user.
- `sudo deluser <username>`: Remove a user.
- `passwd <username>`: Change the password for a user.
- `groups <username>`: Show the groups a user belongs to.

## Process Management
- `ps aux`: Display all running processes.
- `top`: Show real-time system resource usage.
- `kill <PID>`: Terminate a process by PID.
- `htop`: Interactive process viewer (if installed).

## Networking
- `ip a`: Show IP addresses.
- `ping <host>`: Test connectivity to a host.
- `netstat -tuln`: Display listening ports and connections.
- `traceroute <host>`: Trace the network route to a host.
- `curl -I <URL>`: Fetch HTTP headers of a URL.

## Package Management (Debian/Ubuntu)
- `sudo apt update`: Update package lists.
- `sudo apt upgrade`: Upgrade all packages.
- `sudo apt install <package>`: Install a package.
- `sudo apt remove <package>`: Remove a package.

## Permissions
- `chmod <permissions> <file>`: Change file permissions.
  - Example: `chmod 755 file.sh`
- `chown <user>:<group> <file>`: Change ownership of a file.
  - Example: `chown user:group file.txt`
