from socket import *
#IMPORTS
#######################
c = socket(AF_INET, SOCK_STREAM)
hostport = ('localhost', 38447)

c.connect(hostport)
#ENVIANDO O ENDERECO DE CLIENTE E PORTA PARA O ACCEPT NO SERVIDOR
##################################
while True:

    try:

        msg = input("Client request: ")

        c.send(msg.encode())
#CODIFICANDO REQUISIÇAO DO CLIENTE E ENVIANDO PARA O SOCKET DO SERVIDOR
#####################################
        chat = c.recv(1024).decode()
        print("receive from Server: " + chat)

    except ConnectionAbortedError:

        print("Conexao encerrada")
        break

c.close()


c.close()
