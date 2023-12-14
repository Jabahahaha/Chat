import socket

socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 33124
server_address = '127.0.0.1'

socket_one.connect((server_address, port))

while True:
    request = input("You: ")
    socket_one.send(request.encode())

    if request.lower() == "stop":
        break

    response = socket_one.recv(4096)
    print("Server:", response.decode())

socket_one.close()
