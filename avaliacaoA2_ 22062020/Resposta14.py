poema = (input('Digite o trecho de uma poema por favor: ').lower())
poema = poema.replace('a','$')
poema = poema.replace('e','$')
poema = poema.replace('i','$')
poema = poema.replace('o','$')
poema = poema.replace('u','$')
print(poema)