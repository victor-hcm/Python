from random import randint
menor = 0
maior = 0
n = (randint(1, 10), randint(1, 10), randint(1, 10),
    randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {n}')
print(f'O menor valor mostrado foi {min(n)}') #funciona em tuplas
print(f'O maior valor mostrado foi {max(n)}')