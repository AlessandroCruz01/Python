from datetime import datetime
while True:
    try:
        dia = int(input('Dia: '))
        if not 1 <= dia <= 31:
            raise ValueError('Valor fora do intervalo permitido')
        break
    except ValueError as error:
        print(error)
while True:
    try:
        mes = int(input('Mes: '))
        if not 1 <= mes <= 12:
            raise ValueError('Valor fora do intervalo permitido')
        break
    except ValueError as error:
        print(error)

while True:
    try:
        ano = int(input('Ano: '))
        if not 1000 <= ano <= 9999:
            raise ValueError('Valor fora do intervalo permitido')
        break
    except ValueError as error:
        print(error)
data1 = '{}/{}/{}'.format(dia,mes,ano)
hoje = datetime.now()
data = datetime.strptime(data1, '%d/%m/%Y').date()
futuro = datetime.fromordinal(hoje.toordinal()-data.toordinal())
print('Voce tem hoje exatamente {} anos'.format(futuro.year))