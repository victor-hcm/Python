print('-=-' * 20)
print('Analisador de Trinângulos')
print('-=-' * 20)
r1 = float(input('Primero segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo:!')
    if r1 == r2 and r2 == r3: # if r1 == r2 == r3 também dar certo em python
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
            print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

