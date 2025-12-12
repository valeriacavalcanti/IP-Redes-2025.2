matriz = []

for i in range(4):
    matriz.append([0] * 4)

# percorrer todos os índices da matriz e atribuir o valor 10
# para cada elemento.

for i in range(4):
    for j in range(4):
        matriz[i][j] = i * j

print(matriz)
for i in range(4):
    for j in range(4):
        print(i, j, matriz[i][j])

for i in range(4):
    print(matriz[i])
