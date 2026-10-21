"""The Grim Repositioner: local server.

    python serve.py            -> http://127.0.0.1:8139/

Serves only the app (index.html, vendor/, brand/), never docs or tooling. The app also runs
straight from a double-clicked index.html; the server is just a convenience.
"""
import os
import re
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")
if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = 8139
ALLOWED = re.compile(r"^/(?:index\.html|vendor/[\w.\-/]+|brand/[\w.\-/]+)?$")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def do_GET(self):
        p = self.path.split("?", 1)[0].split("#", 1)[0]
        if ".." in p or not ALLOWED.match(p):
            self.send_error(404)
            return
        super().do_GET()

    def do_HEAD(self):
        self.do_GET()


if __name__ == "__main__":
    print("The Grim Repositioner -> http://127.0.0.1:%d/" % PORT)
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
