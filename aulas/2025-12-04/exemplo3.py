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

if ((simbolo >= '0') and (simbolo <= '9')):
    print('é um símbolo numérico')
elif ((simbolo >= 'A') and (simbolo <= 'Z')):
    print('é uma letra maiúscula')
elif ((simbolo >= 'a') and (simbolo <= 'z')):
    print('é uma letra minúscula')
else:
    print('caractere especial')
