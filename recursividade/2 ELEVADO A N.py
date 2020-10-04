def valor(n):
    if n == 1:
        return 2
    elif n == 0:
        return 1
    else:
        print(2*valor(n-1))
        valor(n-1)



valor(3)
