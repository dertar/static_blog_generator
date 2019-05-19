from http.server import HTTPServer, SimpleHTTPRequestHandler

def main(port = 80):
    httpd = HTTPServer(('',port),SimpleHTTPRequestHandler)
    print('Serving at port:{0}'.format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server down!")

main()
