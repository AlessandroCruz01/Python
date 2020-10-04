def fatorial(n):
    if n == 1:
        print("Pronto")
    else:
        return n*(fatorial(n-1))
        
fatorial(5)        
        