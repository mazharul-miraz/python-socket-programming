import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREM)
s.connect(socket.gethostname(), 1024)
msg =s.recv(1024)
print(msg.decode("utf-8"))
