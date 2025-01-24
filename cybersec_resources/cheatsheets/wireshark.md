# Wireshark Cheat Sheet

## Common Filters
- `ip.addr == <IP>`: Filter packets by IP address.
- `tcp.port == <port>`: Filter packets by TCP port.
- `udp.port == <port>`: Filter packets by UDP port.
- `http`: Display only HTTP traffic.
- `dns`: Display only DNS queries and responses.

## Advanced Filters
- `ssl.handshake`: Filter SSL/TLS handshake packets.
- `tcp.stream eq <n>`: Follow a specific TCP stream.
- `frame contains <keyword>`: Search for packets containing a specific keyword.
- `icmp`: Display ICMP (ping) traffic.
- `arp`: Show ARP requests and replies.

## Display Filters
- `ip.src == <IP>`: Show packets with a specific source IP.
- `ip.dst == <IP>`: Show packets with a specific destination IP.
- `eth.src == <MAC>`: Filter packets with a specific source MAC address.
- `eth.dst == <MAC>`: Filter packets with a specific destination MAC address.
- `tcp.flags.syn == 1`: Display packets with the SYN flag set.

## Capture Filters
- `host <IP>`: Capture traffic to/from a specific IP.
- `net <subnet>`: Capture traffic within a subnet (e.g., `net 192.168.1.0/24`).
- `port <port>`: Capture traffic on a specific port (e.g., `port 80`).
- `tcp`: Capture only TCP packets.
- `udp`: Capture only UDP packets.

## Useful Shortcuts
- **Follow TCP/UDP Stream:** Right-click a packet and select `Follow > TCP/UDP Stream`.
- **Statistics:** Navigate to `Statistics > Protocol Hierarchy` to view traffic breakdown.
- **Export Packets:** Use `File > Export Objects` to extract files transferred over HTTP or other protocols.

## Performance Tips
- **Enable Packet Coloring:** Go to `View > Coloring Rules` to enable traffic patterns visualization.
- **Filter Large Captures:** Use `Capture > Options` to limit capture size or duration.
- **Save Filters:** Save commonly used filters for quick access.

---
