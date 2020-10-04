from time import sleep
idades = []
idade = 1
while idade != 0:
    try:
        idade = int(input('Digita idade: '))
        if idade == 0:
            break
    except ValueError:
        print('Somente valores inteiros')

    idades.append(idade)

idade = 0
print(idades)
idades = sorted(set(idades))
for i in idades:

    print('\033[0;34m',i,end=' ')
    sleep(2)
