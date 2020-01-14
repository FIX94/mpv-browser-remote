import http.server
import socket
import sys

def doMpvCmd(thecmd):
    try:
        if isWindows:
            f=open(r'\\.\pipe\mpv-pipe','wb')
            f.write(thecmd)
            f.close()
        else:
            client = socket.socket(socket.AF_UNIX)
            client.connect('/tmp/mpv-socket')
            client.send(thecmd)
            client.close()
    except IOError:
        #keeping silent in case mpv is not open
        pass

class ourServer(http.server.BaseHTTPRequestHandler):
    def doGetResponse(self, isGet):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            if isGet == True: #file read in before
                self.wfile.write(our_index_html)
        else: #only got a root file
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        self.doGetResponse(True)
            
    def do_HEAD(self):
        self.doGetResponse(False)

    def do_POST(self):
        if self.path == '/play':
            doMpvCmd(b'cycle pause\n')
        elif self.path == '/quit':
            doMpvCmd(b'quit\n')
        elif self.path == '/fw10':
            doMpvCmd(b'seek 10\n')
        elif self.path == '/bw10':
            doMpvCmd(b'seek -10\n')
        elif self.path == '/fw60':
            doMpvCmd(b'seek 60\n')
        elif self.path == '/bw60':
            doMpvCmd(b'seek -60\n')
        #204 cause we dont send any body back
        self.send_response(204)
        self.end_headers()

    def log_message(self, format, *args):
        #keeping the server silent
        return

#quick platform check
print('Is on Windows:')
isWindows = sys.platform.startswith('win');
print(isWindows)

#read in our displayed index.html
print('Reading in index.html')
f=open('index.html','rb')
our_index_html = f.read()
f.close()

#start server on any ip at port 8000
address = ('', 8000)
httpd = http.server.HTTPServer(address, ourServer)
print('Starting server')
httpd.serve_forever()
