import socket
import ssl

def query_server(host: str, port: int, query: str, use_ssl: bool = False) -> str:
    """

    Args:
      host: str: 
      port: int: 
      query: str: 
      use_ssl: bool:  (Default value = False)

    Returns:

    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if use_ssl:
            context = ssl.create_default_context()
            sock = context.wrap_socket(sock, server_hostname=host)

        sock.connect((host, port))
        sock.sendall(query.encode("utf-8"))
        response = sock.recv(1024).decode("utf-8")
        return response
    except Exception as e:
        return f"ERROR: {e}"
    finally:
        sock.close()

if __name__ == "__main__":
    HOST = "135.181.96.160"  # Replace with server IP
    PORT = 44445         # Replace with server port
    QUERY = "2;0;23;21;0;22;3;0;"
    USE_SSL = False       # Set to False if SSL is disabled

    print(query_server(HOST, PORT, QUERY, USE_SSL))