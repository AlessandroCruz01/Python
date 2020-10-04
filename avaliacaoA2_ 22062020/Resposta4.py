while True:
    try:
        a1 = int(input("Digita um numero inteiro: "))
        a2 = int(input("Digita outro numero inteiro: "))
        a3 = int(input("Digita outro numero inteiro: "))
        a4 = int(input("Digita outro numero inteiro: "))
        a5 = int(input("Digita outro numero inteiro: "))
        break
    except ValueError:
        print("Voce digitou um tipo de dado errado.")

print(a1,a2,a3,a4,a5)
a1 *= a1
a2 *= a2
a3 *= a3
a4 *= a4
a5 *= a5
tup = (a1,a2,a3,a4,a5)

print(tup)

