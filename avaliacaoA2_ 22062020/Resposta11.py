import json
from datetime import *
nome = str(input("Nome: "))
nAnimal = None
dados = {}
geral = []
id = 1
while nAnimal != 'x':
    nAnimal = str(input('Nome do animal: '))
    dados.update({id:nAnimal})
    id += 1
data = datetime.now()
data = data.strftime('%d/%m/%Y %H:%M')
geral.append({nome:dados, 'Data/Hora':data})
print(geral)

try:
    with open('cadastro.json', 'w') as f:
        json.dump(geral, f, indent=4)
        print("ok")
        f.close()
except:
    print('Problemas ao abrir arquivo')
