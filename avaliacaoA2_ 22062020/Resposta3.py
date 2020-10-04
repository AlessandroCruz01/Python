
while True:
    try:
        a1 = int(input("Digita um numero inteiro: "))
        a2 = int(input("Digita outro numero inteiro: "))
        break
    except ValueError:
        print("Voce digitou um tipo de dado errado.")
print('Forma que foi digitada:','\033[3;33;45m', a1,',', a2 ,'\033[3;33;45m')

#para o terminal voltar ao normal:
print('\033[0;0m')