#Coloquei o import hashlib
import hashlib


#f = open("/etc/passwd", "r")
with open('C:/Users/ntorresa/Desktop/FIAP/88.Codes/FIAP_ON/FASE_4_CTF/arq.txt', 'r') as file:
   linha_lida_do_arq = file.read()


#Passar apenas os 4 primeiros caracteres do arquivo /etc/passwd 
print(linha_lida_do_arq[0]+linha_lida_do_arq[1]+linha_lida_do_arq[2]+linha_lida_do_arq[3])
#hashvalue = arquivo[0,4]
hashvalue = linha_lida_do_arq[0]+linha_lida_do_arq[1]+linha_lida_do_arq[2]+linha_lida_do_arq[3]

#Criptografa usando HASH SHA256

hashobj1 = hashlib

#result = hashobj1.update(hashvalue.encode())
result = hashobj1.sha256(hashvalue.encode())


#Imprime o HASH SHA256
print(result.hexdigest())