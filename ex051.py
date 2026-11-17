primeiro = int(input('Primeiro termo: ')) #de onde começar
razão = int(input('Razão: ')) #quantidade de casas a pular (Ex: 5, pula cinco números)
decimo = primeiro + (10 - 1) * razão #mostrar os 10 primeiros termos de acordo com a entrada do usuário
for c in range(primeiro, decimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('ACABOU')