from socket import *

socketcliente = socket(AF_INET, SOCK_STREAM)
hostport = ('localhost', 24883)
socketcliente.connect(hostport)

print(f'INICIANDO ALMIRCHAT')
while True:
    chat = input("Cliente: ")

    try:
        socketcliente.sendall(bytes(chat, 'utf -8'))
    except ConnectionAbortedError:
        print("Sua mensagem nao será encaminhada pois o servidor encerrou a conexao.")
        socketcliente.close()
        break
socketcliente.close()
