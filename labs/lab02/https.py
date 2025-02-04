#!/usr/bin/python3
# https.py

from socket import *
import sys
import select

sock = socket()
sock.bind(("0.0.0.0",9000))
sock.listen()
(newsock, addr) = sock.accept()
print("connection from", addr)

while True:
    socklist = [newsock, sys.stdin]  ## focus here!!!
    (r_sockets, w_sockets, e_sockets) = select.select(socklist, [], [])

    if e_sockets:     ## an error took place --> stop the loop
        break

    if newsock in r_sockets:   # we have something to read from new sock!
        data = newsock.recv(1024)
        data = data.decode()[:-1]
        if not data:  # no data means the connection has been closed.
            break
        print(data)

        method, path, _ = data.split(" ", 2)
        print(path)
        path = path.strip("/")
        print(path)
        if method == "GET":
            try:
                if(path == "" or path == "favicon.ico"):
                    with open("index.html", "r") as f:
                        content = f.read()
                else:
                    with open(path, "r") as f:
                        content = f.read()

                response = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/html\r\n"
                        f"Content-Length: {len(content)}\r\n"
                        "\r\n"
                        f"{content}"
                        )
                newsock.sendall(response.encode())
            except Exception:
                response = (
                        "HTTP/1.1 404 Not Found\r\n"
                        "Content-Type: text/html\r\n"
                        )
                print("finna kill this foo")
                newsock.sendall(response.encode())
                print("after")
    if sys.stdin in r_sockets:  # we have something to read from sys.stdin!
        s = sys.stdin.readline()  # we need to use the low-level function readline()
        newsock.send(s.encode())


newsock.close()
sock.close()
