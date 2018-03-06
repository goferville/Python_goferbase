"""
tcp socket need to monitor receiving data length.
Here an ending word b'exit' is used to judge the end of message
this ending message must  do time.sleep(0.1)
to separate with main message to be identified\
otherwise it will not be received separately and need extra parsing
"""
import socket


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
svr_host='192.168.0.19'
svr_port=80
tcp_svr(svr_host,svr_port)




