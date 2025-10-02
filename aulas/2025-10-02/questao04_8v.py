mes = int(input('Informe o código do mês: '))


if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
   print(31)
else:
    if mes == 2:
        print(29)
    else:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            print(30)
        else:
            print('inválido')
