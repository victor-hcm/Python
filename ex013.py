desconto = float(input('Digite o valor do produto: R$'))
novo = desconto - (desconto * 5 / 100)
print('O produto custava R${}, na promoção com desconto de 5% vai custar R${}'.format(desconto, novo))