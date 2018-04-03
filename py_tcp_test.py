import socket, time


def rcvall(sc, nB):
    data=b''
    #print("receiving sub")
    while len(data)<nB:
        more=sc.recv(5000)
        #print("length of data:", more)
        if more==b'exit':
            print("Receiving complete before target length!")
            break
        data+=more
    return data


def tcp_svr(svr_host, svr_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind((svr_host, svr_port))
    sock.listen(1)
    while True:
        print("Server waiting")
        try:
            (sc, addr)=sock.accept()
        except:
            print('accpt() error!')
            break
        print('call received!')
        while True:
            print("in coming connection from:", sc.getpeername())
            message=rcvall(sc,100)

            print("In-coming message: ", message.decode('utf-8'))
            sc.sendall(b'Message receiving ... ...')
            # message='1000'
            if message=='0001':
                otext="End request received, session complete!"
                print(otext)
                sc.sendall(otext.encode())
                sc.close()

def tcp_client(svr_host, svr_port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((svr_host,svr_port))
    print("Client sock name=", sock.getsockname())
    text=b'Hello from lab7133!\n\r'
    #data=text.encode()
    sock.sendall(text)
    text1='This is Goferville! Add-ons are small apps you can add to Firefox that do lots of things — from managing to-do lists, to downloading videos, to changing the look of your browser.'
    text =text1.encode('utf-8')
    sock.sendall(text)
    time.sleep(0.1)
    text=b'exit'
    sock.sendall(text)

    time.sleep(100)

# svr_host='192.168.0.19'
svr_host='10.34.59.168'
svr_port=6000
tcp_client(svr_host,svr_port)
#tcp_svr(svr_host,svr_port)
