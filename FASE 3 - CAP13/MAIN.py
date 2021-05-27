#importando módulo hashlib
import hashlib

#importando módulo getpass para 
from getpass import getpass

#importando módulo do arquivo lista_users.py (que contem a função )
import lista_users

#recebe na variavel "lista_carregada" o retorno da função "load_users"
lista = lista_users.load_users

#Recebe usuario digitado capturando na variavel "user"
user = input("Digite o username: ")

#Recebe senha digitada capturando na variavel "senhacrypt",
# utilizando o getpass o inves do input para ocultar a senha durante a digitação 
# onde ela é transformada em bytes (Função "encode")
# para então ser enviada função de criptografia "sha256" do módulo "hashlib",
# o resultado da função "sha256" então é convertido ao final em hexadecimal com a função "hexdigest"
senhacrypt = hashlib.sha256(getpass("Digite sua senha: ").encode()).hexdigest()

#Leitura da lista carregada utilizando a variavel "regdict" para armazenar os registros da lista,
# assim que a variavel "regdict" recebe a linha da lista ela se torna de classe "dict" (dicionario de dados)
for reg in lista():
    if user == (reg["username"]):
        #Quando o usuário(digitado) for igual ao usuario(da lista)
        # deve ir para a validação de senha
        if (senhacrypt) == (reg["password"]):
            #Quando a senha criptografada(digitada) bater com a senha criptografada(da lista)
            # deve exibir nome do usuario e que ele esta logado 
            print ("{} Logado!".format(reg["name"]))
            break
        else:
            #Caso a senha seja inválida deve exibir mensagem "Usuário/Senha Inválida"
            print ("Usuário/Senha Inválida")
            break
    else:
        #Quando o usuário(digitado) não for encontrado nos usuarios(da lista)
        # e o index atual da lista é igual ao numero de itens da lista, ou seja a lista chegou ao fim,
        # deve exibir a mensagem "Usuário/Senha Inválida"
        if (lista().index(reg) == (len(lista()) - 1) ):
            print ("Usuário/Senha Inválida")
        