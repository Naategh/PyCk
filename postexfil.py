#!/usr/bin/env python
import http.server as http

class Rq_handler(http.BaseHTTPRequestHandler):
    # to define a request for the base handler the pattern is
    # do_<method>
    def do_POST(self):
        content_len = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_len)
        #open file as wb to write out raw bytes
        log_file = open("outfile.txt","wb")
        log_file.write(post_data)
        log_file.close()
        print("Wrote contents to file")
        self.send_response_only(200)

def main():
    httpd = http.HTTPServer(('0.0.0.0',8000),Rq_handler)
    try:
        print("Recv running on port 8000")
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("Done")

if __name__ == "__main__":
    main()
