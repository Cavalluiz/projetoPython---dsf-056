frase = str(input('Digite uma frase: ')).strip().upper() # variavel para o usuario escolher o texto. strip para retirar os espaços e uppe para deixar tudo maisculo
palavras = frase.split() # split serve para separar as palavras da frase.
junto = ''.join(palavras) # join serve para juntar as palavras da frase.
inverso = ''
for letra in range(len(junto) -1, -1, -1): # definindo a leitura da frase de trás para frente.
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto: # definindo se é um palíndromo.
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')