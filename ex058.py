from random import randint
from time import sleep
computador = randint(0,10) #faz o computador "PENSAR"
print('---' * 20) #ex028 com o comando while
print('Vou pensa em um número entre 0 e 10. Tente adivinhar...')
print('---' * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? ')) #jogador tenta adivinhar
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. ')
print('Acertou com {} tentativas, PARABÉNS!'.format(palpites))

