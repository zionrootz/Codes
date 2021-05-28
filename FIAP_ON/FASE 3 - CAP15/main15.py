import requests

#URL: https://dc1-2021.glitch.me/getHash
#RM: 87856
#Senha: vAwCNf2nbe
#Obs: Antes de começar a acessar a API, acesse https://dc1-2021.glitch.me/ com seu navegador web primeiro. Como o serviço é gratuito, ele fica 'dormente' quando ninguém está usando...

dictjson = {
"RM": 87856,
"Senha": "vAwCNf2nbe"}


r = requests.post('https://dc1-2021.glitch.me/getHash', json=dictjson)
r.status_code
r.text
print(r.text)
