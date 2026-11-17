valores = []
for v in range(0, 5):
    v = int(input('Digite um valor: '))
    valores.append(v)
maior = max(valores)
menor = min(valores)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
