import datetime
cont = 0
ano_atual = datetime.date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nome = str(input('Digite seu nome: '))
    ano_nasc = int(input('Digite sua data de nascimento: '))
    idade = ano_atual - ano_nasc
    print(f"{nome} nasceu em {ano_nasc} sua idade é {idade}")
    if idade >= 21:
        maior = idade - 21
        print(f'Já é maior de idade, fazem {maior}.')
    else:
        menor = 21 - idade
        print(f'\033[31mAinda nao atingiu maior idade, faltam {menor} anos.\033[m')
    if idade >=21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maior de idade.')
print(f'E também tivemos {totmenor} pessoas menores de idade.')
