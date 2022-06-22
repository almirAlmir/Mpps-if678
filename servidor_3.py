from socket import *
import time
import sys

rcvdmessage = bytes("received succesfully", 'utf-8')
hostport = ('localhost', 27156)
s = socket(family=AF_INET, type=SOCK_DGRAM)
s.bind(hostport)

print("Servidor pronto para conexao na porta {}".format(hostport[1]))

while True:
    message, address = s.recvfrom(1024)

    chat = message.decode()
    if chat == 'Encerrar':
        print("Encerrando conexão em breve")
        time.sleep(10)
        break
    elif chat == 'Me diga as horas':
        horas = time.ctime()
        horas = horas.split()

        print(horas[3])

    elif chat == 'Em que ano estamos?':
        print("Estamos em 2022, o ano do Hexa")
    else:
        print("Mensagem: "+chat)
    #print("Endereco remetente: {}".format(address))

    s.sendto(rcvdmessage, address)
s.close()