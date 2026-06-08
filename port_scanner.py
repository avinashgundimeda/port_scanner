import socket
import sys
import time
import threading
from collections import defaultdict

usage = "python3 port_scanner.py TARGET start_port end_port"
print("_"*70)
print("")
print(r'''
  ____  ____  _____ _   _   ____   ___  ____ _____ ____
 / __ \|  _ \| ____| \ | | |  _ \ / _ \|  _ \_   _/ ___|
| |  | | |_) |  _| |  \| | | |_) | | | | |_) || | \___ \
| |__| |  __/| |___| |\  | |  __/| |_| |  _ < | |  ___) |
\____/|_|   |_____|_| \_| |_|    \___/|_| \_\|_| |____/
''')
print("Port Scanner")
print("           *****   CREATED BY Avinash Gundimeda   *****")
print("_"*70)

if len(sys.argv) != 4:
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

# Common port-to-service mapping
PORT_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    587: "SMTP",
    993: "IMAPS",
    995: "POP3S",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
    27017: "MongoDB",
    6379: "Redis",
    9200: "Elasticsearch"
}

print(f"Scanning target: {target}")
print(f"Port range: {start_port} - {end_port}")
print("-" * 70)

threads = []
open_ports = defaultdict(str)
lock = threading.Lock()
start_time = time.time()

def get_service_name(port):
    """Get service name for a port"""
    try:
        return socket.getservbyport(port)
    except OSError:
        return PORT_SERVICES.get(port, "Unknown")

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            service = get_service_name(port)
            with lock:
                open_ports[port] = service
                print(f"Port {port:5d} is OPEN   ({service})")
        s.close()
    except Exception:
        pass

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.daemon = True
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

elapsed_time = time.time() - start_time

print("-" * 70)
print(f"\nScan Results:")
print(f"Total ports scanned: {end_port - start_port + 1}")
print(f"Open ports found: {len(open_ports)}")
print(f"Time elapsed: {elapsed_time:.2f} seconds")

if open_ports:
    print(f"\nOpen Ports Summary:")
    for port in sorted(open_ports.keys()):
        print(f"  {port:5d} - {open_ports[port]}")

print("-" * 70)