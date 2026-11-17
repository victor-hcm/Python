n = int(input('Digite um número para calcular seu Fatorial: '))
c = n #unidade contadora recebe o número do usuário
f = 1
print('Calculando {}! = '.format(n), end='')# end= '' para continuar na mesma linha.
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1 #mesma coisa de c = c - 1
print('{}'.format(f))
