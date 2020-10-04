nomes = []
for i in range(3):
    nomes.append(str(input("nome: ").lstrip().strip().capitalize()))
print(nomes)
print('\033[7m',len(nomes))
