simbolo = input('Digite um símbolo: ')
codigo_decimal = ord(simbolo)
codigo_binario = bin(codigo_decimal)
codigo_octal = oct(codigo_decimal)
codigo_hexa = hex(codigo_decimal)

print(f'{simbolo=}')
print(f'{codigo_decimal=}')
print(f'{codigo_binario=}')
print(f'{codigo_octal=}')
print(f'{codigo_hexa=}')

if ((codigo_decimal >= 48) and (codigo_decimal <= 57)):
    print('é um símbolo numérico')
elif ((codigo_decimal >= 65) and (codigo_decimal <= 90)):
    print('é uma letra maiúscula')
elif ((codigo_decimal >= 97) and (codigo_decimal <= 122)):
    print('é uma letra minúscula')
else:
    print('caractere especial')
