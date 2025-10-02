mes = int(input('Informe o código do mês: '))


if mes >= 1 and mes <= 12:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        print(31)
    elif mes == 2:
        print(29)
    else:
        print(30)
else:
    print('inválido')
