import socket

socket_one = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 33123

socket_one.bind(("0.0.0.0", port))
socket_one.listen(1)

connected_socket, addr = socket_one.accept()
user_name = connected_socket.recv(4096).decode()
print(f"Connection from {user_name} at {addr}")

while True:
    received_data = connected_socket.recv(4096)
    print(f"{user_name}: {received_data.decode()}")

    if "exit" in received_data.decode().lower():
        break

    response = input("You: ")
    connected_socket.send(response.encode())

    if response.lower() == "exit":
        break

connected_socket.close()
socket_one.close()
