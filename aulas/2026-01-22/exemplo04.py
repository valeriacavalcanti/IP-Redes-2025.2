arq = open('teste.csv', 'r')

conteudo = arq.read().splitlines()
    
arq.close()

for linha in conteudo:
    nome, idade = linha.split(',')
    idade = int(idade)
    print(f'{nome=} {idade=}')
