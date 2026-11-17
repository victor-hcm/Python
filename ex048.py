soma = 0 #variavel é acumuladora
cont = 0 #variavel contadora
for c in range (1, 501, 2 ):
    if c % 3 == 0:
        cont = cont + 1 #mesmo signifcado cont += 1
        soma = soma + c #mesmo significado soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))