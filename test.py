from socket import *


def test_req(server_name: str, port: int, test_name: str, req: str):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(("127.0.0.1", port))
    sock.send(req.encode("utf-8"))

    res = b""
    while True:
        new_bytes = sock.recv(1024)
        if len(new_bytes) == 0:
            break
        res += new_bytes

    sock.close()

    WIDTH = 72
    return f"""{f' {test_name} [{server_name}] '.center(WIDTH, '-')}
{res.decode()}
{'-' * WIDTH}
"""


def test(server_name, port):
    testcases = [
        (
            "Normal",
            f"GET / HTTP/1.1\r\nHost: 127.0.0.1:{port}\r\n\r\n",
        ),
        (
            "No Host header",
            f"GET / HTTP/1.1\r\n\r\n",
        ),
        (
            "Multiple Host headers",
            "GET / HTTP/1.1\r\nHost: first.com\r\nHost: second.com\r\n\r\n",
        ),
        (
            "Space-preceded Host as first header",
            "GET / HTTP/1.1\r\n Host: space-preceded-first.com\r\n\r\n",
        ),
        (
            "Space-preceded Host header after another Host",
            "GET / HTTP/1.1\r\nHost: first.com\r\n Host: space-preceded-after-another.com\r\n\r\n",
        ),
        (
            "Non-first space-preceded the only Host header",
            "GET / HTTP/1.1\r\nAccept: */*\r\n Host: non-first-space-preceded-only.com\r\n\r\n",
        ),
        (
            "Space-after-colon Host header",
            "GET / HTTP/1.1\r\nHost:  space-after-colon.com\r\n\r\n",
        ),
        (
            "Space-succeeded Host header",
            "GET / HTTP/1.1\r\nHost: space-succeeded.com \r\n\r\n",
        ),
        (
            "Empty Host header",
            "GET / HTTP/1.1\r\nHost:  \r\n\r\n",
        ),
        (
            "Empty Host header with line-folding",
            "GET / HTTP/1.1\r\nHost:  \r\n \r\n\r\n",
        ),
    ]

    for testcase in testcases:
        print(test_req(server_name, port, testcase[0], testcase[1]))


test("Node http", 3000)
test("Python http.server", 3001)
test("Django", 3002)
test("Rust hyper", 3003)
test("Go", 3004)
test("Ruby Sinatra", 3005)
test("PHP", 3006)
