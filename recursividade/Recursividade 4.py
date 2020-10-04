def parOuImpar(n):
    if n%2 == 0:
        print("par")
        return parOuImpar(n-1)
    else:
        print("impar")
        return parOuImpar(n-1)
        
parOuImpar(10)