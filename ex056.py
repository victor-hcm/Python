somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print('-------- {}ª PESSOA --------'.format(p))
    nome = str(input('Digite o nome: '.format(p))).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual o seu sexo? (M/F) ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade #ele recebe todos os masculinos inseridos
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade #recebe o masculino com a maior idade
        nomevelho = nome #recebe o nome do masculino mais velho
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho é o {}, ele tem {} anos.'.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))