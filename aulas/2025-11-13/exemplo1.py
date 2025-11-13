soma = 0
qtd = 0
numeros = [0,0,0,0,0,0]

for i in range(6):
    numeros[i] = int(input('Número: '))
    soma = soma + numeros[i]

media = soma / (i + 1)

for i in range(len(numeros)):
    if numeros[i] > media:
        qtd = qtd + 1

print(soma)
print(media)
print(numeros)
print(qtd)
