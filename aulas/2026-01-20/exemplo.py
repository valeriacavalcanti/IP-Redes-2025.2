def contar_espacos(texto: str) -> int:
    qtd = 0
    for i in range(len(texto)):
        if texto[i] == ' ':
            qtd += 1
    return qtd


def limpar_espacos(texto: str) -> str:
    novo_texto = texto
    while novo_texto.find('  ') >= 0:
        novo_texto = novo_texto.replace('  ', ' ')

    return novo_texto.strip()

def limpar_espacos_2(texto: str) -> str:
    lista = texto.split()
    return ' '.join(lista)

def contar_palavras(texto: str) -> int:
    novo_texto = limpar_espacos(texto)
    return contar_espacos(novo_texto) + 1

def contar_palavras_2(texto: str) -> int:
    return len(texto.split())

# main
texto1 = 'feliz ano novo 2026 eeee'
texto2 = '    feliz   ano    novo    2026     eeee   '

#print(limpar_espacos(texto2))

#print(contar_espacos(texto1))
#print(contar_espacos(texto2))

#print(contar_palavras(texto2))
#print(contar_palavras_2(texto2))

print(limpar_espacos_2(texto1))
print(limpar_espacos_2(texto2))


