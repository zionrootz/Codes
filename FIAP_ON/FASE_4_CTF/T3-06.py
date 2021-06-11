#Criar uma estrutura em Python que some apenas os números presentes nesta lista que sejam menores que o período de rotação (rotation_period) 
# do planeta Yavin IV do universo Star Wars (essa informação pode ser acessível via API, em https://swapi.dev/api/planets/3/). 
# Exemplo, o número 34 não será somado, mas o 3 e o 1 sim.. A FLAG é o número total desta soma.

import requests
import json

numeros = [34, 3, 1, 51, 6, 33, 23, 2, 29, 5, 33, 1, 7, 65, 4, 12, 5, 7, 46, 3, 41, 15, 3, 23, 2, 1, 3, 21, 35, 4, 6, 2, 13, 5, 14, 10, 3, 25, 7, 13, 14, 7, 5, 33, 21]
valor=0

r = requests.get('https://swapi.dev/api/planets/3/')
#print(r.text)

# Transformando o texto em json recebido da API em dicionario de dados com a função loads do Módulo Json
textdict = json.loads(r.text)

print('nome=',textdict["name"])
print('rotation_period=',textdict["rotation_period"])
print('orbital_period=',textdict["orbital_period"])
print('diameter=',textdict["diameter"])
print('climate=',textdict["climate"])
print('gravity=',textdict["gravity"])
print('terrain=',textdict["terrain"])
print('surface_water=',textdict["surface_water"])
print('population=',textdict["population"])
print('residents=',textdict["residents"])
print('films=',textdict["films"])

rotation_period_int=int(textdict["rotation_period"])
valor=0
for num in numeros:
    if num < rotation_period_int:
        valor=valor+num

print("Valor Final: ", valor)