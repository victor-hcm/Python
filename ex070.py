print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += +1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'. format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {total}')
print(f'Temos {totmil} produto custando mais de R$1000.00')
print(f'O produto mais barato foi o {barato} que custa R${menor}')