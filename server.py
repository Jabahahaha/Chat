import socket

socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 33124

socket_one.bind(("0.0.0.0", port))
socket_one.listen(1)

while True:
    connected_socket, addr = socket_one.accept()
    print("Connection from: " + str(addr))

    while True:
        received_data = connected_socket.recv(4096)
        print("Client:", received_data.decode())

        if "stop" in received_data.decode().lower():
            break

        response = input("You: ")
        connected_socket.send(response.encode())

    connected_socket.close()

    if response.lower() == "stop":
        break

socket_one.close()
