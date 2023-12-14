import socket

socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 33123
server_address = '127.0.0.1'

user_name = input("Enter your name: ")
socket_one.connect((server_address, port))

socket_one.send(user_name.encode())

while True:
    request = input(f"{user_name}: ")
    socket_one.send(request.encode())

    if request.lower() == "exit":
        break

    response = socket_one.recv(4096)
    print(response.decode())

socket_one.close()
