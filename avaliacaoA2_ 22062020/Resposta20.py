from time import sleep
def digita():
    cont = ''
    list = []
    while cont !='x':
        cont = input('Digita: ')
        if cont == 'x':
            break
        try:
            cont=int(cont)
        except ValueError:
            print("Somente numeros: ")
        list.insert(0, cont)
        print(list)
    for i in list:
        print('\033[4;34;47m',i)
        sleep(1)
digita()