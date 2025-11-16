#PROGRAMA PARA SABER QUAL A MEDIA E SE ESTA APROVADO, EM RECUPERAÇÃO OU REPROVADO.
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua nota média foi {media}')
if media < 5.0:
    print('Abaixo da média: REPROVADO')
elif media >=5.0 and media <=6.9:
    print('RECUPERAÇÃO.')
else:
    print('está na média: APROVADO.')
