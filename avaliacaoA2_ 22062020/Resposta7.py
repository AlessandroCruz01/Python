from Funcao import quadrado
import random
numbers = []
for i in range(5):
    numbers.append(random.randint(1,100))
numbers.reverse()
print(numbers)
for i in numbers:
    print('O numero {} tem seu quadrado igual a:'.format(i))
    quadrado(i)