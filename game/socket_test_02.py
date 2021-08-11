#!/usr/bin/env python

# WS server example

import os
from http.server import HTTPServer, CGIHTTPRequestHandler

os.chdir('.')

server_object = HTTPServer(server_address=('',8899),
RequestHandlerClass=CGIHTTPRequestHandler)

server_object.serve_forever()
