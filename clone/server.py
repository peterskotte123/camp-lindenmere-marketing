import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit, unquote

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "camplindenmere.com")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def translate_path(self, path):
        parts = urlsplit(path)
        p = unquote(parts.path)
        q = unquote(parts.query)
        base = os.path.normpath(os.path.join(ROOT, p.lstrip("/")))
        if not base.startswith(ROOT):
            return ROOT
        ext = os.path.splitext(p)[1]
        candidates = []
        if p.endswith("/"):
            candidates.append(os.path.join(base, "index.html"))
        candidates.append(base)
        if q:
            candidates.append(base + "?" + q)
            if ext:
                candidates.append(base + "?" + q + ext)
        candidates.append(base + ".html")
        candidates.append(os.path.join(base, "index.html"))
        for c in candidates:
            if os.path.isfile(c):
                return c
        return base

    def log_message(self, fmt, *args):
        if args and str(args[1]) not in ("200", "304"):
            super().log_message(fmt, *args)


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
