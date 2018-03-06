import argparse, socket
from datetime import datetime
MAX_BYTES = 65535
def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('192.168.0.19', port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        sock.sendto(data, address)
        i=0
        while True:
            text="Currently processing "+str(i)
            data = text.encode('ascii')
            sock.sendto(data, address)
            i+=1
            if i>1000:
                break

def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'The time is {}'.format(datetime.now())
    data = text.encode('ascii')
    sock.sendto(data, ('192.168.0.31', port))
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES) # Danger!
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))
port=50000
#client(port)
server(port)
