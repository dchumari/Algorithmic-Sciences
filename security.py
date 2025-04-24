import ssl

def enable_ssl(server_socket: socket.socket):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    return context.wrap_socket(server_socket, server_side=True)