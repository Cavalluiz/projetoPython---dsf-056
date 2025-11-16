somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0
for i in range(1, 5):
    print(f'----- {i}ª pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A media de idade do grupo é de {mediaidade}')
print(f'O homem mais  velho tem {maioridade} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')