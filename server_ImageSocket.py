import socket
import sys, errno
hostname = '127.0.0.1'
port = 7777
image_name = "image%s.png"
imgcounter = 1

server = socket.socket()
server.bind((hostname, port))
server.listen(5)
print("waiting connect")

buffer_size = 4096

connect_socket, client_address = server.accept()
print(client_address, "connecting")

while True:
    txt = None
    print("waiting for new event")
    receive_content = connect_socket.recv(buffer_size)
    txt = receive_content.decode("utf-8")
    if txt.startswith('SIZE'):
        tmp = txt.split()
        size = int(tmp[1])

        print('size is %s' % size)
        connect_socket.send(bytes("GOT SIZE", encoding="utf-8"))
        # Now set the buffer size for the image
        print('got size')
        buffer_size = 40960000

        my_file = open(image_name % imgcounter, 'ab')
        while True:
            receive_content = connect_socket.recv(buffer_size)
            my_file.write(receive_content)
            if not receive_content:
                break
            print("write file finish")
            my_file.close()
            connect_socket.send(bytes("GOT IMAGE", encoding="utf-8"))
            print("send got image ")
            break
    elif txt.startswith('BYE'):
        connect_socket.shutdown()
    if not receive_content:
        buffer_size = 4096
        connect_socket.send(bytes("server get content success", encoding="utf-8"))
        print("no content...")
        break


print("close connect")
connect_socket.close()

