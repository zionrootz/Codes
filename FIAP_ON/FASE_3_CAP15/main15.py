import requests
import json

#URL da API: https://dc1-2021.glitch.me/getHash
#RM: 87856
#Senha: vAwCNf2nbe
#Obs: Antes de começar a acessar a API, acesse https://dc1-2021.glitch.me/ com seu navegador web primeiro. 
# Como o serviço é gratuito, ele fica 'dormente' quando ninguém está usando...

#Criando dicionario de dados contendo as informações do meu RM e senha recebidos para esta atividade
my_rm_pass = { 
    "rm": 87856, 
    "senha": "vAwCNf2nbe"
}

# Chamando API utilizando função Post do Módulo Requests
r = requests.post('https://dc1-2021.glitch.me/getHash', my_rm_pass)
# Obtendo Status Code
r.status_code

# Transformando o texto em json recebido da API em dicionario de dados com a função loads do Módulo Json
textdict = json.loads(r.text)

# Declarando uma varivel com o conteudo da mensagem de erro para comparação com texto recebido
msg_erro = {"erro":"RM/senha inválidos"}

# Se o texto recebido é diferente da mensagem de erro exibe o Nome e Senha Hash recebidos da API
if textdict != msg_erro:
    print("Nome: {}".format(textdict["nome"]))
    print("Senha_hash: {}".format(textdict["hash"]))
# Senão exibe a mensagem de erro recebida da API
else:
    print(textdict['erro'])
