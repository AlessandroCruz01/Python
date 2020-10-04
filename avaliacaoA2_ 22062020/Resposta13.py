musica = str(input('Digite o trecho de uma musica por favor: '))
musica = musica.split()
lista = []
for i in musica:
    lista.append(str(i))

print(lista)
for i in lista[::-1]:
    print(i, end=' ')