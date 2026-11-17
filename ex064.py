num = 0
cont = 0 #mostrar quantos números foram digitados.
soma = 0 #para mostrar a soma dos número digitados
num = int(input('Digite um número [999 para parar]: ')) #função fora para que ele conte somente os números sem o 999
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma deles é igual a {}'.format(cont, soma))