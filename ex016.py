km = float(input('Qual a quantidade de Km percorridos? '))
dias = int(input('Quantos dias ficou com o carro? '))
custo = (dias*60) + (km * 0.15)
print('O valor do aluguel é de R$ {}'.format(custo))