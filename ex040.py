n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.2f} e {:.2f}, a média do aluno é {}'.format(n1, n2, media))
if media < 5.0:
    print('Aluno REPROVADO!')
elif 7 > media >= 5.0:
    print('Aluno em Recuperação!')
elif media >= 7.0:
    print('Aluno APROVADO!')
