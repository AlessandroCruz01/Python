def soma(lista):
    if len(lista)==1:
        return (lista[0])
    else:
        return lista[0]+soma(lista[1:])

soma([1,2,3])