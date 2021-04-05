import sys
import socket



HOST = sys.argv[1]
PORT = int(sys.argv[2])

try:
    FILE_PATH = sys.argv[3]
except IndexError:
    FILE_PATH = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    request_string = "GET /" + FILE_PATH + " HTTP/1.1\r\nHost:" + HOST + "\r\n\r\n" 
    s.send(request_string.encode())
    res = s.recv(4096)
    print(res.decode('UTF-8'))