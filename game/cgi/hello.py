#!/usr/bin/python3
# The line above ^ is important. Don't leave it out. It should be at the
# top of the file.

import cgi, cgitb # Not used, but will be needed later.

print("Content-type: text/html\n\n")
print("hello world!")

html = open("./checkers.html", "r")

print(html.read())
