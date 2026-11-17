sexo = str(input('Informa seu sexo: [M/F] ')).strip().upper()[0] #[0] fatiamento para pegar a primeira letra digitada pelo usuário.
while sexo not in 'MnFf': #quando o usuário digitar as letras, vai seguir o comando abaixo.
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))