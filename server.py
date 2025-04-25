"""
Server implementation for handling concurrent TCP connections and searching strings in a file.
"""

import socket
import threading
import time
import ssl
import re
from typing import Optional
import configparser
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load configuration
config = configparser.ConfigParser()
config.read("config.ini")

LINUX_PATH = config.get("settings", "linuxpath")
REREAD_ON_QUERY = config.getboolean("settings", "REREAD_ON_QUERY")
SSL_ENABLED = config.getboolean("settings", "SSL")
PORT = config.getint("settings", "port")
HOST = config.get("settings", "host")

# Preload file if REREAD_ON_QUERY is False
if not REREAD_ON_QUERY:
    with open(LINUX_PATH, "r") as f:
        lines = set(f.read().splitlines())


def handle_client(conn: socket.socket, addr: tuple) -> None:
    """Handles incoming client connections and processes search queries.

    Args:
      conn(socket.socket): Client connection socket.
      addr(tuple): Client IP address and port.
      conn: socket.socket: 
      addr: tuple: 

    Returns:
      : None

    """
    try:
        # Receive query
        data = conn.recv(1024).decode("utf-8").strip("\x00")
        start_time = time.time()

        # Log request
        logging.debug(
            f"Query='{data}' from IP={addr[0]} at {time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        # Search logic
        result = "STRING NOT FOUND\n"
        if REREAD_ON_QUERY:
            with open(LINUX_PATH, "r") as f:
                if data in f.read().splitlines():
                    result = "STRING EXISTS\n"
        else:
            if data in lines:
                result = "STRING EXISTS\n"

        # Send response
        conn.sendall(result.encode("utf-8"))

        # Log execution time
        exec_time = (time.time() - start_time) * 1000
        logging.debug(f"Execution time={exec_time:.2f}ms")

    except FileNotFoundError as e:
        logging.error(f"File not found - {e}")
        conn.sendall(b"SERVER ERROR\n")
    except socket.error as e:
        logging.error(f"Socket error - {e}")
        conn.sendall(b"SERVER ERROR\n")
    except Exception as e:
        logging.error(f"Unexpected error - {e}")
        conn.sendall(b"SERVER ERROR\n")
    finally:
        conn.close()


def start_server() -> None:
    """Starts the server and listens for incoming connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    if SSL_ENABLED:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile="server.crt", keyfile="server.key")
        server = context.wrap_socket(server, server_side=True)

    logging.info(f"Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    start_server()