# programa para ler a média e informar se passou direto por média.

media = int(input('Informe a média: '))
frequencia = int(input('Informe a frequencia: '))

if media >= 70:
    if frequencia >= 75:
        print('Passou por média')
    else:
        print('Reprovado por falta')
else:
    if frequencia >= 75:
        print('Não passou por nota')
    else:
        print('Reprovador por nota e frequencia')
