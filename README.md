# String Search Server

This project implements a high-performance TCP server that searches for strings in a large text file. The server supports concurrent connections, configurable file reading behavior, SSL authentication, and robust logging. It is designed to handle files with up to 1,000,000 lines efficiently.

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the Server](#running-the-server)
6. [Testing](#testing)
7. [Performance Report](#performance-report)
8. [Security](#security)
9. [Contributing](#contributing)
10. [License](#license)

---

## Features
- **Concurrent Connections**: Handles an unlimited number of concurrent client requests using multithreading.
- **Configurable File Reading**: Supports both cached and real-time file reading (`REREAD_ON_QUERY` option).
- **SSL Authentication**: Configurable SSL/TLS encryption for secure communication.
- **Robust Logging**: Logs queries, client IPs, execution times, and errors with timestamps.
- **High Performance**: Optimized for fast string search in large files (up to 1 million lines).
- **PEP8 Compliance**: Clean, well-documented, and PEP8-compliant code.

---

## Requirements
- Python 3.8 or higher
- Linux operating system
- A text file (e.g., `200k.txt`) containing searchable strings
- Dependencies listed in `requirements.txt`

---

## Installation

### Step 1: Clone the Repository
```bash
git https://github.com/dchumari/Algorithimic-Sciences
cd string-search-server
```

### Step 2: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 3: Place the Text File
Place the `200k.txt` file (or any other dataset) in the desired directory. Update the `config.ini` file with the correct path.

### Step 4: Configure the Server
Edit the `config.ini` file to specify:
- `linuxpath`: Path to the text file.
- `REREAD_ON_QUERY`: Set to `True` or `False` depending on whether the file should be re-read on every query.

Example `config.ini`:
```ini
linuxpath=/path/to/200k.txt
REREAD_ON_QUERY=False
```

### Step 5: Run the Server
Start the server manually:
```bash
python server.py
```
Or install it as a daemon using the provided script:
```bash
bash install.sh
```
---

### Generating SSL Certificates
To create `server.crt` and `server.key`, run:
```bash
openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes


## Running the Server

### Manual Start
Run the server directly:
```bash
python server.py
```


---

### **9. Exception Handling**
Make exception handling more specific.

**Fix:**
Update `server.py`:
```python
except FileNotFoundError as e:
    logging.error(f"File not found: {e}")
except ValueError as e:
    logging.error(f"Invalid input: {e}")
except Exception as e:
    logging.error(f"Unexpected error: {e}")

### Daemon Mode
Use the `install.sh` script to run the server as a Linux service:
```bash
bash install.sh
```

The server listens on `0.0.0.0:44445` by default. You can change the host and port in `server.py`.

---

## Testing

### Unit Tests
Run all unit tests using `pytest`:
```bash
pytest tests/
```

### Client Script
Use the `client.py` script to send queries to the server:
```bash
python client.py <host> <port> <query>
```
Example:
```bash
python client.py 127.0.0.1 44445 "example_string"
```

### Concurrency Test
Simulate multiple clients using tools like `ab` (Apache Benchmark):
```bash
ab -n 1000 -c 100 http://127.0.0.1:44445/
```

### Stress Test
Use tools like `locust` or `wrk` to simulate high traffic:
```bash
locust -f locustfile.py --host=http://127.0.0.1:44445
```

---

## Performance Report

The `speed_report.pdf` contains detailed benchmarks of different search algorithms, including:
- Linear search
- Binary search (for sorted files)
- Regex matching
- Set-based search
- Mmap-based search

The report includes:
- A table comparing execution times for various file sizes.
- A chart showing performance trends as the file size increases.

---

## Security

### SSL Authentication
Enable SSL by setting `ssl_enabled=True` in `server.py` and providing a self-signed certificate (`server.crt` and `server.key`).

### Input Validation
The server handles oversized payloads, null bytes, and malformed inputs securely.

### Buffer Overflow Protection
All inputs are sanitized to prevent buffer overflow attacks.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or feedback, contact:
- Email: dchumari@gmail.com
- GitHub: [GitHub Profile](https://github.com/dchumari)

---



```
