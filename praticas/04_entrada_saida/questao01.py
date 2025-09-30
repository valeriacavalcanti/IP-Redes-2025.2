valor_pago = float(input('Informe o valor pago: '))
valor_desconto = float(input('Informe o valor do desconto: '))

valor_compra = valor_pago + valor_desconto

aliquota_desconto = (valor_desconto * 100) / valor_compra

#print('Desconto:', aliquota_desconto, '%')
#print(f'Desconto: {aliquota_desconto:.2f}%')
print(f'Desconto: {aliquota_desconto:.1f}%')
