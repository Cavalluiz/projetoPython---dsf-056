soma = 0 # Acumulador para somar os valores solicitados
cont = 0 # Contador para identificar quantos numeros na repetição foram identificados para a soma
for i in range(1, 501, 2): # para encontrar os numeros impares foi coloca passo = 2, para repetição contar de 2 em 2.
    if i % 3 == 0:
        soma = soma + i
        cont = cont + 1
print(f'A soma de todos os {cont} valores solicitados é {soma}.')