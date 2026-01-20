LINHAS = 2
COLUNAS = 2

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
        if matriz[i][j] not in numeros_distintos:
            numeros_distintos.append(matriz[i][j])

# exibir os diferentes valores
print(numeros_distintos)
