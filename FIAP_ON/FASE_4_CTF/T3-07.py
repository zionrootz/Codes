#Criar uma estrutura em Python percorra o dicionário de palavras e conte quantas palavras começam com a letra “a”.

palavras = ['exercício', 'girafa', 'abençoado', 'urso', 'tatu', 'raiz', 'zebra' 'baço', 'tamanduá', 'banana', 'gigante', 'abarrotando', 'destino', 'amor', 'caju', 'dança', 'juri', 'bafo', 'palhaço', 'travesseiro', 'gelo', 'abismavam', 'santinho', 'abalar', 'dolorido', 'aba', 'abra', 'tarde', 'gás', 'abaixo', 'jacaré', 'urina', 'amarelo', 'gênero', 'canja', 'balaio', 'abacateiro', 'uísque', 'abandonarei', 'joio', 'noite', 'gêmeos', 'baixo', 'ralo', 'herói', 'utopia', 'amanhã', 'judô', 'ganho', 'último', 'aborígene', 'loiro', 'alergia', 'manhã', 'prêmio', 'abajur', 'débil', 'abnegar', 'ultraje', 'garimpo', 'abacaxi', 'abismo', 'balão', 'geografia', 'maravilhoso', 'fada', 'abdômen', 'abolição', 'editor', 'gênero', 'xadrez', 'aborto', 'sábio', 'abaco', 'abdominal', 'elevador', 'galo', 'abelha', 'aborrecer', 'azul', 'dado', 'rato', 'ablativo', 'fila', 'egoísta', 'abacate', 'uva', 'abraço', 'elegante', 'abarcar', 'raro', 'ajuste', 'avó', 'sapo', 'abutre', 'uso', 'editora']


ct=0
for linha in palavras:
    if linha[0] == 'a':
        print(linha)
        ct=ct+1

print("Qt palavras que começam com a: ", ct)
