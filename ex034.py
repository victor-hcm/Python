salario = float (input('Qual o valor do seu salário? '))
print('...Calculando o seu aumento...')
if salario <= 1250:
    novo = salario + (salario * 15 / 100) #aumento de 15%
else:
    novo = salario + (salario * 10 / 100) #aumento de 10%
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))