"""Serve the static ValleyballHistory.com site locally.

This project is a static website and is ready for GitHub Pages.
Run this file with Python to start a local HTTP server.
"""

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os
import webbrowser

PORT = 8000

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    url = f"http://localhost:{PORT}/"
    print(f"Serving static site at {url}")
    print("Press Ctrl+C to stop.")

    try:
        webbrowser.open(url)
    except Exception:
        pass

    with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
