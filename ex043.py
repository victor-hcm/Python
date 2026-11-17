peso = float(input('Qual o seu peso? (KG) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está OBESO.')
else:
    print('OBESIDADE MÓRBIDA.')