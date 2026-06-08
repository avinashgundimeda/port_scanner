# Open Ports - Python Port Scanner

A fast multithreaded TCP port scanner written in Python.

## Features

- Multithreaded scanning
- Custom port range scanning
- Service detection
- DNS hostname resolution
- Scan statistics
- Open port summary
- Lightweight and easy to use

---

## Screenshot

```bash
Scanning target: 192.168.1.1
Port range: 1 - 1000

Port 22    is OPEN   (SSH)
Port 80    is OPEN   (HTTP)
Port 443   is OPEN   (HTTPS)

Scan Results:
Total ports scanned: 1000
Open ports found: 3
```

---

## Requirements

- Python 3.x

No external libraries are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/open-ports.git
cd open-ports
```

---

## Usage

```bash
python3 port_scanner.py TARGET START_PORT END_PORT
```

### Example

```bash
python3 port_scanner.py scanme.nmap.org 1 1000
```

### Output

```bash
Port 22    is OPEN   (SSH)
Port 80    is OPEN   (HTTP)
Port 443   is OPEN   (HTTPS)
```

---

## Supported Services

| Port | Service |
|--------|----------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 445 | SMB |
| 3306 | MySQL |
| 3389 | RDP |
| 5432 | PostgreSQL |
| 5900 | VNC |
| 6379 | Redis |
| 8080 | HTTP-Alt |
| 9200 | Elasticsearch |
| 27017 | MongoDB |

---

## Warning

Use this tool only on:

- Systems you own
- Systems you have permission to test

Unauthorized scanning may violate laws and regulations in your country.

---

## Author

**Avinash Gundimeda**

Cybersecurity Student

---

## License

MIT License