num = int(input('Digite um número: ')) #vai ler um número e dizer se é primo!
tot = 0
for c in range(1, num + 1): #vai de 1 até o número digitado, por isso o num + 1
    if num % c == 0:
        print('\033[33m', end='') #cor amarela
        tot += 1 #mesma coisa tot = tot + 1
    else:
        print('\033[31m', end='') #cor vermelha
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso que ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
