frase = str(input('Digite uma frase: ')).strip().upper() #1ª função tira os espaços e a segunda para maiúsculo.
palavras = frase.split() #função dividir ou separar um texto (string) em partes menores, transformando-o em uma lista.
junto = ''.join(palavras)
inverso = ''
#inverso = junto[::-1] elimina o for e funciona da mesma forma.
for letra in range(len(junto) - 1, -1, -1): #inverso da entrada do usuário
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('A frase digitada não é um Palíndromo')
