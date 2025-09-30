hora = int(input('Informe a hora: '))
minuto = int(input('Informe o minuto: '))
segundo = int(input('Informe o segundo: '))

tempo = hora * 3600 + minuto * 60 + segundo

print(f'Tempo em segundos = {tempo}')