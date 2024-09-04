# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
from filelock import FileLock


class localWeb(BaseHTTPRequestHandler):
    def do_GET(self):
        p = "web/local"
        qu = self.path.find("?")
        if qu == len(self.path) - 1:
            self.path = self.path[:-1]
            qu = -1
        if qu == -1:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            if self.path == "/":
                self.wfile.write(
                    open(p + self.path + "index.html").read().encode("utf-8")
                )
            else:
                try:
                    self.wfile.write(open(p + self.path).read().encode("utf-8"))
                except FileNotFoundError:
                    self.wfile.write(open(p + "/" + "404.html").read().encode("utf-8"))
        else:
            self.path = self.path[qu + 1:]
            args = {i[: i.find("=")]: i[i.find("=") + 1 :] for i in self.path.split("&")}
            
        print(self.path)

    def do_POST(self):
        pass


class publicWeb(BaseHTTPRequestHandler):
    def do_GET(self):
        p = "web/public"
        pass

    def do_POST(self):
        pass


def startLocalWeb():
    httpd = HTTPServer(("", 8080), localWeb)
    httpd.serve_forever()


def startPublicWeb():
    httpd = HTTPServer(("", 8081), publicWeb)
    httpd.serve_forever()
