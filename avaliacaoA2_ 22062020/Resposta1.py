dados_originais = []
novos_dados = []
controle = ''
while controle != 'bicicleta':
    controle = input('Digita: ')
    if controle == 'bicicleta':
        novos_dados = dados_originais
        dados_originais = None
    elif controle not in dados_originais:
        dados_originais.append(controle)
    else:
        print('repetido')

print(dados_originais)
print(novos_dados)