import socket
import threading
from typing import Optional
from config_parser import parse_config
from search_handler import SearchHandler
# from security import enable_ssl
import logging

logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def enable_ssl(server_socket: socket.socket):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    return context.wrap_socket(server_socket, server_side=True)

class Server:
    def __init__(self, host: str, port: int, ssl_enabled: bool):
        self.host = host
        self.port = port
        self.ssl_enabled = ssl_enabled
        self.config = parse_config()
        self.search_handler = SearchHandler(self.config['linuxpath'], self.config['REREAD_ON_QUERY'])
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if self.ssl_enabled:
            self.server_socket = enable_ssl(self.server_socket)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(100)
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()

    def handle_client(self, client_socket: socket.socket, client_address: tuple):
        try:
            start_time = time.time()
            payload = client_socket.recv(1024).decode('utf-8').strip('\x00')
            query = payload.strip()
            logging.info(f"Received query '{query}' from {client_address}")
            result = self.search_handler.search(query)
            response = f"{result}\n"
            client_socket.sendall(response.encode('utf-8'))
            logging.info(f"Query '{query}' processed in {time.time() - start_time:.4f} seconds")
        except Exception as e:
            logging.error(f"Error handling client {client_address}: {e}")
        finally:
            client_socket.close()



if __name__ == "__main__":
    HOST = "7;0;1;28;0;9;3;0;"
    PORT = 44445
    SSL_ENABLED = False  # Can be overridden by config
    server = Server(HOST, PORT, SSL_ENABLED)
    server.start()