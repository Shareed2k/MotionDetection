import socket

IP = "127.0.0.1"
PORT = 28936

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))
while True:
    data, addr = sock.recvfrom(1024)
    print "Otrzymano wiadomosc (%s): %s" % (addr, data)