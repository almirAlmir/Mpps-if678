import time
from socket import *
#IMPORTS
##############################
s = socket(AF_INET, SOCK_STREAM)
hostport = ('localhost', 38447)
s.bind(hostport)
s.listen(1)
#CRIACAO SOCKET, CONECTANDO A PORTA 38447 E PREPARANDO PRA OUVIR 1 CONEXAO
##################################

closewarnings = 1;
#VARIAVEL PRA CONTROLAR QTD DE TIMEOUTS POSSIVEIS
####################

con, addr = s.accept()
print("Servidor conectado a {} na porta {}".format(addr[0], hostport[1]))
con.settimeout(15)
while True:


    try:
        chat = con.recv(1024).decode()
        print(f"{chat}")
        closewarnings = 1
        con.settimeout(15)
        print("Server sending -> ")
        con.send(input().encode())
        con.settimeout(15)
    except timeout:
        if closewarnings > 0:

            closewarnings = closewarnings - 1
            #DECREMENTANDO A UNICA WARNING DISPONIVEL
            #########################
            print("Caso não haja requisição dentro de 5 segundos a conexão será encerrada")

            con.settimeout(5)


        else:

            con.close()
            break


con.close()

