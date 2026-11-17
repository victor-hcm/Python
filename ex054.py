from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totmaior +=1
    else:
        totmenor +=1
print('A quantidade de maiores foi {}'.format(totmaior))
print('A quantidade de menores foi {}'.format(totmenor))
