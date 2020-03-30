import socket
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
    print("waiting for new event")
    receive_content = connect_socket.recv(buffer_size)
    txt = receive_content.decode("utf-8")
    if txt.startswith('SIZE'):
        tmp = txt.split()
        size = int(tmp[1])

        print('size is %s' % size)
        connect_socket.send(bytes("GOT SIZE", encoding="utf-8"))
        # Set the buffer size for the image
        print('got size')
        buffer_size = 40960000

        # write file
        my_file = open(image_name % imgcounter, 'wb')
        while True:
            receive_content = connect_socket.recv(buffer_size)
            my_file.write(receive_content)
            if not receive_content:
                break
            print("writing to file finished")
            my_file.close()
            connect_socket.send(bytes("SERVER GOT IMAGE", encoding="utf-8"))

            buffer_size = 4096
            imgcounter += 1
            break
    elif txt.startswith('BYE'):
        connect_socket.close()


connect_socket.close()

