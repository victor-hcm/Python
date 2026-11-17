lista = ('Lápis', 2,
         'Caderno', 15.50,
         'Estojo', 25.50,
         'Borracha', 2.50,
         'Caneta', 1.50,
         'Mochila', 100.00,
         'Lapiseira', 7.50)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')#40 espaços centralizados
print('-' * 40)
for pos in range(0, len(lista)): #len(lista) para ir até o final da lista
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='') #alinha o texto para esquerda com 30 espaços com pontos
    else:
        print(f'R${lista[pos]:>7.2f}')