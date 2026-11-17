num = cont = soma = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break #para parar a repetição e ler somente os digitados antes do 999.
    cont += 1
    soma += num
print('Você digitou {} números e a soma deles é {}.'.format(cont, soma))