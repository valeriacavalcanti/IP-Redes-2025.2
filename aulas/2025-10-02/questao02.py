nome1 = input('Nome da primeira pessoa: ')
idade1 = int(input('Idade da primeira pessoa: '))

nome2 = input('Nome da segunda pessoa: ')
idade2 = int(input('Idade da segunda pessoa: '))

if idade1 > idade2:
    print(nome1)
else:
    # idade1 NÃO é maior
    if idade2 > idade1:
        print(nome2)
    else:
        # idade2 NÃO é maior
        print('idades iguais')
