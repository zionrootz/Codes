
def funcao(n):

#arrumei a identação do if dentro da função
#faltava um = na validação
#falatava o ":" no if e else e identações incorretas
    if (n == 1):
        return n
    else:
        return n*funcao(n-1)

print(funcao(19))