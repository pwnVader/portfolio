# Metasploit Framework Cheat Sheet

## Basic Commands
- `msfconsole`: Start the Metasploit console.
- `search <keyword>`: Search for exploits or modules.
- `use <module>`: Select a module to use.
- `show options`: Display module options.
- `set <option> <value>`: Set a module option.
- `exploit`: Launch the exploit.
- `sessions -i <id>`: Interact with a session.

## Post Exploitation (Meterpreter)
- `sysinfo`: Display target system info.
- `getuid`: Display user info.
- `upload <file> <path>`: Upload a file to the target.
- `download <file>`: Download a file from the target.
- `shell`: Open a command shell on the target system.

## Scanning and Discovery
- `db_nmap <options>`: Use Nmap within Metasploit.
- `auxiliary/scanner/portscan/tcp`: Perform a TCP port scan.
- `auxiliary/scanner/http/http_version`: Detect the HTTP server version.

## Exploit Modules
- `exploit/windows/smb/ms08_067_netapi`: Exploit for the MS08-067 vulnerability.
- `exploit/multi/http/tomcat_mgr_deploy`: Exploit for Apache Tomcat Manager.

## Payloads
- `set PAYLOAD windows/meterpreter/reverse_tcp`: Set a reverse TCP payload.
- `set PAYLOAD linux/x86/meterpreter/reverse_tcp`: Set a reverse TCP payload for Linux.

## Database Management
- `db_status`: Check the status of the database.
- `hosts`: List all discovered hosts.
- `services`: List services detected during scans.

## Managing Sessions
- `sessions -l`: List all active sessions.
- `sessions -i <id>`: Interact with a specific session.
- `sessions -k <id>`: Kill a specific session.
- `sessions -K`: Kill all sessions.

## Additional Commands
- `resource <file.rc>`: Run commands from a resource file.
- `history`: Show command history.
- `save`: Save the current workspace.

---
