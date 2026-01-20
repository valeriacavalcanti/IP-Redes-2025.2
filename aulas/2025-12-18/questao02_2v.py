def procurar(lista: list, valor: int) -> bool:
    qtd = 0
    for i in range(len(lista)):
        if lista[i] == valor:
            return True
    return False
    


## PP

LINHAS = 12
COLUNAS = 12

numeros_distintos = []

# declarar a matriz
matriz = []
for i in range(LINHAS):
    matriz.append([0] * COLUNAS)

# ler os valores e armazenar na matriz
for i in range(LINHAS):
    for j in range(COLUNAS):
        matriz[i][j] = int(input(f'Valor({i}-{j}): '))

# identificar os diferentes valores armazenados na matriz
for i in range(LINHAS):
    for j in range(COLUNAS):
        if procurar(numeros_distintos, matriz[i][j]) == False:
            numeros_distintos.append(matriz[i][j])

# exibir os diferentes valores
print(numeros_distintos)
