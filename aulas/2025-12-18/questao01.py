import random

TAM = 40

posicoes = []

# declarar o vetor
numeros = [0] * TAM

# ler os valores
for i in range(TAM):
    numeros[i] = int(input('Número: '))

# gerar um valor aleatorio
valor = random.randint(1, 100)

# armazenando as posições onde "valor" aparece no vetor
for i in range(TAM):
    if numeros[i] == valor:
        posicoes.append(i)

# verificar se "valor" está na lista
if len(posicoes) == 0:
    print(f'Não tem {valor} na lista')
else:
    print(f'{valor} aparece {len(posicoes)} vezes')
    print('Posicoes:', posicoes)
