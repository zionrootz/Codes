#Criar uma estrutura em Python que multiplique apenas os números em posições ímpares desta lista, ou seja, 
# multiple o primeiro número (34), o terceiro (1), o quinto (6), o sétimo (23), e por aí vai … a FLAG é o resultado desta multiplicação.

numeros = [34, 3, 1, 51, 6, 33, 23, 2, 29, 5, 33, 1, 7, 65, 4, 12, 5, 7, 46, 3, 41, 15, 3, 23, 2, 1, 3, 21, 35, 4, 6, 2, 13, 5, 14, 10, 3, 25, 7, 13, 14, 7, 5, 33, 21]

i = 1
valor=1
for linha in numeros:
    if (i%2) == 0:
        print("Par")
    else:
        print("Ímpar")
        valor=valor*linha
        print('valor: ', valor)
        print('linha: ', linha)
    i=i+1
print('valor final: ', valor)