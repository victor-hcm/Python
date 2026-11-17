frase = str(input('Escreva uma frase: ')).upper().strip() #trabalha a entrada do usuário em maiúsculo e tira os espaços inicio/final
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) #Começa a contagem do final