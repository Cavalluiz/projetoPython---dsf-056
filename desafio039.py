#PROGRAMA PARA DESCOBRIR SE ESTA NA IDADE DE SE ALISTAR OU SE JA PASSOU E QUANTO TEMPO FALTA OU PASSOU.
import datetime
ano_nascimento = int(input('Digite o ano que você nasceu: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento
print(f'Você nasceu em {ano_nascimento}, sua idade é de {idade} anos, em {ano_atual}, ano atual.')
if idade > 18:
    tempo = idade - 18
    alist_ano = ano_atual - tempo
    print(f'Há {tempo} anos, deveria ter se alistado ao serviço militar obrigatório.')
    print(f'Seu alistamento foi em {alist_ano}.')
elif idade < 18:
    tempo = 18 - idade
    alist_ano = ano_atual + tempo
    print(f'Você ainda não está na idade de se alistar, faltam {tempo} anos.')
    print(f'Seu alistamento será em {alist_ano}.')
else:
    print('Você ja está na idade de se alistar para o serviço obrigatório militar.')
