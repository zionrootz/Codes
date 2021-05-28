import requests
import json

#URL da API: https://dc1-2021.glitch.me/getHash
#RM: 87856
#Senha: vAwCNf2nbe
#Obs: Antes de começar a acessar a API, acesse https://dc1-2021.glitch.me/ com seu navegador web primeiro. Como o serviço é gratuito, ele fica 'dormente' quando ninguém está usando...

dictjson = {
"rm": 87856,
"senha": "vAwCNf2nbe"}

r = requests.post('https://dc1-2021.glitch.me/getHash', dictjson)
r.status_code
textdict = json.loads(r.text)

print("Status Code: {}".format(r.status_code))
print("Nome: {}".format(textdict["nome"]))
print("Senha_hash: {}".format(textdict["hash"]))