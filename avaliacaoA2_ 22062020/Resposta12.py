import json
def jsonrite():
    with open('cadastro.json', 'r') as f:
        arq = json.load(f)
        print(arq)
        f.close()
jsonrite()