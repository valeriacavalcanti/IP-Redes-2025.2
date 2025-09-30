valor_compra = float(input('Informe o valor da compra: '))

valor_vista = valor_compra * 0.9
valor_direto = valor_compra
valor_parcelado = valor_compra * 1.2

print(f'Valor à vista: R$ {valor_vista:.2f}')
print(f'Valor direto para 30 dias: R$ {valor_direto:.2f}')
print(f'Valor parcelado: {valor_parcelado:.2f}')
