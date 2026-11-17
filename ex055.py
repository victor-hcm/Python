pesomaior = 0
pesomenor = 0
for p in range(1, 6):
    pessoa = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        pesomaior = pessoa
        pesomenor = pessoa
    else:
        if pessoa > pesomaior:
            pesomaior = pessoa
        if pessoa < pesomenor:
            pesomenor = pessoa
print('O maior peso lido foi de {}Kg'.format(pesomaior))
print('O menor peso lido foi de {}Kg'.format(pesomenor))
