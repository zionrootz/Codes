''' 
Este programa valida se uma frase digitada é um palindromo, 
 ou seja uma frase possui o mesmo sentindo quando lemos ela ao contrario
 
'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('A FRASE DIGITADA É UM PALÍNDROMO')
else:
    print('A FRASE DIGITADA NÃO É UM PALÍNDROMO')
print('FRASE NORMAL   :', junto)
print('FRASE INVERTIDA:', inverso)