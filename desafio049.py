print('''escolha o operador da tabuada:
[1] SOMA
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO''')
o1 = int(input('Digite qual operador: '))
numero = int(input('Digite qual numero para calcular a tabuada: '))
for i in range(1, 11):
    if o1 == 1:
        n = numero + i
        print(f'{numero} + {i} = \033[1;32m{n}\033[m')
    elif o1 == 2:
        n = numero - i
        print(f'{numero} - {i} = \033[1;32m{n}\033[m')
    elif o1 == 3:
        n = numero * i
        print(f'{numero} * {i} = \033[1;32m{n}\033[m')
    elif o1 == 4:
        n = numero / i
        print(f'{numero} / {i} = \033[1;32m{n}\033[m')
    else:
        print('\033[1;31mEscolha invalida!\033[m, tente novamente.')