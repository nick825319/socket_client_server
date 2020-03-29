import socket

ip = '127.0.0.1'

port = 7777

client_socket = socket.socket()
client_socket.connect((ip, port))
print("connect to ", (ip, port))

image_name = "image%s.png"

#content = input("image name (add file Extension name, 'BYE' for disconnect):")
content = image_name = "image%s.png" % 1

# sending test to server
# client_socket.send(bytes(content, encoding='utf-8'))
# recvdata = client_socket.recv(1024)
# print(str(recvdata))

# open file
file = open(image_name, "rb")
file_bytes = file.read()
size = len(file_bytes)

# send size
client_socket.send(bytes("SIZE %s" % size, encoding='utf-8'))
recvdata = client_socket.recv(1024)
print(str(recvdata))
# send image bytes
if recvdata == b"GOT SIZE":
    client_socket.sendall(file_bytes)
    recvdata = client_socket.recv(1024)
    print(str(recvdata))
    client_socket.close()


