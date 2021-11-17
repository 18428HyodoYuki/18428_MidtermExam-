import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SOCK:
    SOCK.connect(('127.0.0.1', 50007))
    SOCK.sendall(b'hello server')
    data = SOCK.recv(1024)
    print(repr(data))
