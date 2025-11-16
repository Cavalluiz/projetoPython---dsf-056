num = int(input('Digite um número: '))
tot = 0 # variavél para identificar quantos numeros sao divisiveis.
for c in range(1, num+1):
    if num % c == 0: # se o numero for divisivel pelo contador
        print('\033[32m', end=' ')
        tot += 1 # se for divisivel é +1 numero no final.
    else:
        print('\033[m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes.', end=' ')

if tot == 2:
    print('\nE por isso ele é PRIMO.')
else:
    print('\nE por isso ele NÃO É PRIMO.')
        