def countdown(n):
    if n == 0:
        return print("Fim")
    else:
        print(n)
        return (countdown(n-1))

countdown(3)