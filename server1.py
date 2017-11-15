import socket
s=socket.socket()
port=12345
s.bind(('', port))
s.listen(5)
while True:
    c, addr=s.accept()
    print('Got connection {}'.format(addr))
    msg='Goferville got your connection!'.encode()
    c.send(msg)
    c.close()