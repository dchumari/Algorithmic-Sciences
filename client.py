import socket
import sys

def query_server(host: str, port: int, query: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(query.encode('utf-8'))
        response = s.recv(1024).decode('utf-8')
        print(response.strip())

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py <host> <port> <query>")
        sys.exit(1)
    query_server(sys.argv[1], int(sys.argv[2]), sys.argv[3])