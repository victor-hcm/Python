salario = float(input('Digite o valor atual do salário: R$'))
novo = salario + (salario * 15 / 100)
print('O valor atual do salário é R${}, com o ajuste de 15% de aumento subiu para R${}'.format(salario, novo))