import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('131.179.77.168', 8080))
client.sendall('I am client\n'.encode())
