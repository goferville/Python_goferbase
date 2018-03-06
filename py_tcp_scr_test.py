import socket


def rcvall(sc, nB):
    data=b''
    while len(data)<nB:
        more=sc.recv(nB-len(data))
        if not more:
            print("Receiving complete before target length!")
            break
    return data


def tcp_svr(svr_host, svr_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind((svr_host, svr_port))
    sock.listen(1)
    while True:
        print("Server waiting")
        sc, addr=sock.accept()
        while True:
            print("in coming connection from:", sock.getpeername())
            message=rcvall(sc,16)
            print("In-coming message: ", message.decode())
            sc.send("Message receiving ......")
            if message=='0001':
                otext="End request received, session complete!"
                print(otext)
                sc.sendall(otext.encode())
                sc.close()
svr_host='192.168.0.19'
svr_port=5000
tcp_svr(svr_host,svr_port)




