from socket import *
import time

socketservidor = socket(AF_INET, SOCK_STREAM)
hostport = ('localhost', 24883)
socketservidor.bind(hostport)
socketservidor.listen(1)

while True:
    print("Servidor Aguardando proxima conexao...")
    con, cliente = socketservidor.accept()
    print("Servidor conectado a HOST {}".format(cliente[0]))
    tempoInicial = time.time()
    while True:
        tempoAtual = time.time()
        if(15-(tempoAtual-tempoInicial) > 0):
            tempoRestante = tempoAtual - tempoInicial
            con.settimeout(15-tempoRestante)
        else:
            con.settimeout(0.00000001)

        try:
            chat = con.recv(1024)
            print(chat.decode())
        except timeout:
            con.close()
            print("Conexao encerrada depois de ultrapassar {:.1f} segundos".format(con.gettimeout()+ tempoRestante))
            break

