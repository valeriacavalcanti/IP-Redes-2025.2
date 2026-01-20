def verificar_minusculo(simbolo: str) -> bool:
    if simbolo >= 'a' and simbolo <= 'z':
        return True
    else:
        return False


def verificar_maiusculo(simbolo: str) -> bool:
    if simbolo >= 'A' and simbolo <= 'Z':
        return True
    else:
        return False

def converter_para_maiusculo(simbolo: str) -> str:
    if verificar_minusculo(simbolo) == True:
        codigo = ord(simbolo)
        codigo = codigo - 32
        return chr(codigo)
    else:
        return simbolo


def converter_para_minusculo(simbolo: str) -> str:
    if verificar_maiusculo(simbolo) == True:
        codigo = ord(simbolo)
        codigo = codigo + 32
        return chr(codigo)
    else:
        return simbolo


## PP

texto = input('Frase: ')
novo_texto = ''

for s in texto:
    if verificar_minusculo(s) == True:
        novo_texto += converter_para_maiusculo(s)
    elif verificar_maiusculo(s) == True:
        novo_texto += converter_para_minusculo(s)
    else:
        novo_texto += s

print(texto)
print(novo_texto)
