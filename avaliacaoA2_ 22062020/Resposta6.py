f = []
nomes = ()
for i in range(10):
    f.append(input("Nome do {}° animal: ".format(i+1)))
nomes = f
print('O nome Rex aparece exatamente {} vez nessa tupla'.format(nomes.count('rex')))
