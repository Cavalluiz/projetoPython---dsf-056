print('Monte uma progressão aritmética.')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite sua razão: '))
for n in range(1, 11):
    an = a1 + (n - 1) * r
    print(an, end=' ')
print('ACABOU')