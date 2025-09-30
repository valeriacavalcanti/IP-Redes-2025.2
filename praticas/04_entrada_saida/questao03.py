qtd_tipo_1 = int(input('Quantidade do tipo 1: '))
qtd_tipo_2 = int(input('Quantidade do tipo 2: '))
qtd_tipo_3 = int(input('Quantidade do tipo 3: '))
qtd_tipo_4 = int(input('Quantidade do tipo 4: '))

valor_compra = (qtd_tipo_1 * 40) + (qtd_tipo_2 * 50) + (qtd_tipo_3 * 80) + (qtd_tipo_4 * 100)

qtd_cupons = valor_compra // 100

print(f'Valor da compra: R$ {valor_compra:.2f}')
print(f'Quantidade de cupons: {qtd_cupons}')
