num = int(input('Digite um número inteiro: '))
resultado = num % 2
if resultado == 0:
    print('Esse número é PAR.'.format(num))
else:
    print('Esse número é IMPAR.'.format(num))