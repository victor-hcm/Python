num = list()
par = list()
ímpar = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        ímpar.append(v)
print(f'Segue a lista dos número digitados: {num}')
print(f'Lista dos números pares digitados: {par}')
print(f'Lista dos números ímpares digitados: {ímpar}')
