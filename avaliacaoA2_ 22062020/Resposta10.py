from time import sleep
lista = []
elementos = ''
while elementos != 'tabela':
    elementos = input("Digita: ")
    lista.append(elementos)

for i in lista:
    print(i)
    sleep(3)