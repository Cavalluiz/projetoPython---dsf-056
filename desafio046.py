from time import sleep
print('Contagem regressiva para o ano novo!')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('      FELIZ ANO NOVO!')

rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0,-1):
        print(end=' ')
    k = k + 1
    for j in range(0, i + 1):
        print('*', end=' ')
    print('')