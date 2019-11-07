import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREM)
s.bind(socket.gethostname(), 1024)
s.listen(5)



while True:
    clt, adr=s.accept()
    print(f"Connection to {adr} established ")
    clt.sned(bytes("Wellcome to socket programming in python", "utf-8" ))
