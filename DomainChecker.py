import os
import socket

list_email = ("")
print("Digite os servidores separados com virgula (Ex: outlook.com,gmail.com:")
list_email = input(list_email).split(",")
lista = list()
for n in list_email:
    try:

        socket.gethostbyname(n)
    except:
        print(n + ": é um domínio inexistente e foi salvo na lista invalidos")
        arquivo = open('invalidos.txt', 'a')
        arquivo.write(n)
        arquivo.write("\n")