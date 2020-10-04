def cadastrar():
    cpf = ''
    dados = {}
    while cpf != 'x':
        cpf = input("Digita: ")
        if len(cpf)<15:
            cpf= '{}'.format('0'*(15-len(cpf))+cpf) #JURO QUE NEM SEI COMO TIVE ESSA IDEIA!
            print(cpf)
        try:
            cpf = int(cpf)
        except ValueError:
            print("No cpf so podem numeros manim!")
            continue
        nome = input('Nome: ')
        if nome.isdigit() == True:
            print('Só letras manim: ')
            continue

        dados.update({cpf:nome})
        print(dados)

cadastrar()
