from datetime import date #Puxa a data atual da máquina
atual = date.today().year #Puxa o ano atual
nasc = int(input('Digite o seu ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade < 18:
    saldo = 18 - (atual - nasc)
    alistamento = saldo + atual
    print('Ainda faltam {} anos para o alistamento!'.format(saldo))
    print('Seu alistamente será em {}'.format(alistamento))
elif idade == 18:
    saldo = 18 - idade
    print('Você tem que se alistar imediatamente!'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    alistamento = atual - saldo
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(alistamento))