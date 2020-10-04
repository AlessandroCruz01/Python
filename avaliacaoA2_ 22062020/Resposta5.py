a1 = str(input("Digita um animal: "))
a2 = str(input("Digita outro animal: "))
a3 = str(input("Digita outro animal:  "))
animais = (a1,a2,a3)
for i in animais:
    print('\033[0;31m'+i)