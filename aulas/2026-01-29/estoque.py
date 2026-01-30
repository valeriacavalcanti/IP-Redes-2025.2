# abrir o arquivo para leitura
arq = open('estoque.csv', 'r')
conteudo = arq.read().splitlines()
arq.close()

# quantidade de linhas do arquivo
qtd_linhas = len(conteudo)

# quantidade de produtos
qtd_produtos = qtd_linhas - 1 # retirar o tituto

# valor total do meu estoque
valor_estoque = 0

# lista para armazenar TODOS os produtos que estao no arquivo
lista_produtos = []

for i in range(1, len(conteudo)):
    #print(i, type(conteudo[i]), conteudo[i])
    dados = conteudo[i].split(',')
    #print(i, produto)
    
    produto = {}
    produto['descricao'] = dados[0]
    produto['valor'] = float(dados[1])
    produto['quantidade'] = int(dados[2])
    produto['peso'] = int(dados[3])

    lista_produtos.append(produto)

    valor_estoque += (produto['valor'] * produto['quantidade'])
    
print(f'{qtd_linhas = }')
print(f'{qtd_produtos = }')
print(f'{valor_estoque = }')


# exibir todos os produtos armazenados na memória principal (na lista)

for i in range(len(lista_produtos)):
    print(f"Descricao: {lista_produtos[i]['descricao']}")
    print(f"Valor: {lista_produtos[i]['valor']}")
    print(f"Quantidade: {lista_produtos[i]['quantidade']}")
    print(f"Peso: {lista_produtos[i]['peso']}")
    print('-----------')
