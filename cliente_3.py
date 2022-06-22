from socket import *

serverAddress = ('localhost', 27156)

c = socket(family=AF_INET, type=SOCK_DGRAM)
while True:
    msg = bytes(input("Cliente: "), 'utf-8')
    c.sendto(msg, serverAddress)
    msgFromServer = c.recvfrom(1024)
    chat = (msgFromServer[0]).decode()
    print("Message: "+chat)

