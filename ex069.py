print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
qtdidade = 0
qtdhom = 0
qtdmul = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    if idade >= 18:
        qtdidade += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    continuar = ' '
    if sexo == 'Mm':
        qtdhom += +1
    if sexo == 'F' and idade <20:
        qtdmul += +1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {qtdidade}.')
print(f'Ao todo temos {qtdhom} homens cadastrados')
print(f'E temos {qtdmul} mulheres com menos de 20 anos.')
print('ACABOU!')
