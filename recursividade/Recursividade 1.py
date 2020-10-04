
def contagem_regressiva(n):
    if n == 0:
        print("Fogo")
    else:
        print(n)
        contagem_regressiva(n-1)