import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as A:
    A.bind(('127.0.0.1', 50007))
    while True:
        recvdata, fromaddr = A11.recvfrom(1024)
        print("data: {}, addr: {}".format(recvdata, fromaddr))
        