from http.server import BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):
    #use array for class-wise global variables
    # when array elemnt changed = content in that address changed
    # = class-wise global variable
    vs=[-19.0, 145.0, 1]

    def do_HEAD(self):
        return

    def do_GET(self):
        self.respond()

    def do_POST(self):
        return

    def handle_http(self, status, content_type):

        self.send_response(status)
        self.send_header('Content-type', content_type)
        # self.send_header('Content-type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        print(self.vs[0])
        self.tmpStr=str(self.vs[0])+","+str(self.vs[1])
        if(self.vs[0]>-10):
            self.vs[2]=-1
        elif(self.vs[0]<-19):
            self.vs[2] = 1
        self.vs[0]=self.vs[0]+self.vs[2]*0.3

        return bytes(self.tmpStr, "UTF-8")


    def respond(self):
        content = self.handle_http(200, 'text/html')
        self.wfile.write(content)
