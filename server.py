import socket

HOST = "25.38.92.129"
PORT = 8080

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen()
print("Server is listening on port " + str(PORT))

while True:
    connection, address = serverSocket.accept()

    req = connection.recv(1024).decode()
    # print(req)

    headers = req.split('\n')
    # print(headers[0])
    filename = headers[0].split()[1]

    if (filename == '/'):

        fin = open('index.html')
        content = fin.read()
        fin.close()
        
        res = 'HTTP/1.0 200 OK\n\n' + content
        connection.sendall(res.encode())
        connection.close()
        continue
    
    try:
        fin = open('static' + filename)
        content = fin.read()
        fin.close()

        res = 'HTTP/1.0 200 OK\n\n' + content
        connection.sendall(res.encode())

    except FileNotFoundError: 
        fin = open('static/404.html')
        content = fin.read()
        fin.close()

        res = 'HTTP/1.0 404 NOT FOUND\n\n' + content
        connection.sendall(res.encode())

    connection.close()
serverSocket.close()