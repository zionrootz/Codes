from getpass import getpass
import requests
import json

#Recebe usuario digitado capturando na variavel "user"
a = 0
while a == 0:
    user = input("Digite o RM(somento os numeros): ")
    if user.isnumeric():
       a = 1
    else:
        print("Valor inválido, por favor digite somento os numeros de seu RM")

#Recebe senha digitada 
senha = getpass("Digite sua senha: ")


#URL da API: https://dc1-2021.glitch.me/getHash
#Obs: Antes de começar a acessar a API, acesse https://dc1-2021.glitch.me/ com seu navegador web primeiro. Como o serviço é gratuito, ele fica 'dormente' quando ninguém está usando...

dictjson = {"rm": user, "senha": senha}
msg_erro = {"erro":"RM/senha inválidos"}

r = requests.post('https://dc1-2021.glitch.me/getHash', dictjson)
r.status_code
textdict = json.loads(r.text)

if textdict != msg_erro:
    print ("[ {} Logado! ]".format(textdict["nome"]))
else:
    print('[ {} ]'.format(textdict['erro']))