from random import randint
v = 0
while True:
    numcomputer = randint(0, 10)
    print('-='*30)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-='*30)
    valor = int(input('Diga um valor: '))
    total = valor + numcomputer
    tipo = ' '
    while tipo not in 'PpIi': #enquanto tipo não for ..
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*60)
    print(f'Você jogou {valor} e o computador {numcomputer}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v +=1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')