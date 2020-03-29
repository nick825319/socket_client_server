import socket

ip = '127.0.0.1'
port = 7777

client_socket = socket.socket()
client_socket.connect((ip, port))
print("connect to ", (ip, port))

image_name = "image%s.png"

while True:
    content = input("content (-1:exit):")
    if content == '-1':
        break
    client_socket.send(bytes(content, encoding='utf-8'))
    recvdata = client_socket.recv(1024)
    print(str(recvdata))
client_socket.close()
