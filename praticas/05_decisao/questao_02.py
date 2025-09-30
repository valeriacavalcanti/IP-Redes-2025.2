nome_1 = input('Informe o nome da primeira pessoa: ')
idade_1 = int(input('Informe a idade da primeira pessoa: '))

nome_2 = input('Informe o nome da segunda pessoa: ')
idade_2 = int(input('Informe a idade da segunda pessoa: '))

if idade_1 > idade_2:
    print(f'{nome_1} é mais velha que {nome_2}')
else:
    if idade_2 > idade_1:
        print(f'{nome_2} é mais velha que {nome_1}')
    else:
        print(f'{nome_1} e {nome_2} possuem a mesma idade.')