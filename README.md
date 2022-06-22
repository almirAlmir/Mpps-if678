# Mpps-if678
Atividades relacionadas a cadeira de infra-com do Centro de informática.

Descrição das atividades

Nesta atividade, vocês produzirão programas do tipo cliente-servidor, explanando e exercitando os conceitos de sockets vistos em aula.

Faça um programa cliente-servidor utilizando o protocolo TCP através da porta 24883 em que o servidor deverá apresentar no console as mensagens recebidas do cliente durante 15 segundos após o estabelecimento da conexão, depois disso a conexão com o cliente deverá ser encerrada. Em seguida, o servidor deverá ficar apto a receber uma outra conexão pela mesma porta.

Faça um programa cliente-servidor utilizando o protocolo TCP através da porta 38447, em que o cliente possa enviar e receber mensagens lidas do teclado do servidor, e o servidor possa também enviar e receber mensagens do cliente. Caso o servidor fique sem receber uma nova mensagem por até 15 segundos, a mensagem “Caso não haja requisição dentro de 5 segundos a conexão será encerrada” deverá ser enviada ao cliente; caso dentro de 5 segundos não haja uma requisição do cliente ao servidor, a conexão com o cliente deverá ser encerrada pelo servidor e a mensagem “Conexão encerrada” deve ser enviada do servidor para o cliente e exibida no console do cliente.

Nota: O cliente deverá esperar uma resposta do servidor, antes de enviar uma nova requisição. Enquanto que o servidor deverá aguardar ser contatado para então responder.

Faça um programa cliente-servidor utilizando o protocolo UDP através da porta 27156, em que o servidor deverá apresentar no console todas as mensagens que receber do cliente, e caso venha a receber três mensagens específicas, deverá retornar as seguintes respostas:

“ Me diga as horas”: deverá responder com a hora atual do sistema. 
“Em que ano estamos?”: deverá responder “Estamos em 2022, o ano do Hexa”
“Encerrar”: deverá responder “Encerrando conexão em breve” e após 10 segundos  encerrar a conexão com o cliente.

