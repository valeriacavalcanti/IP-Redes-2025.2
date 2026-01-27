arq = open('teste.csv', 'w')

for i in range(4):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    arq.write(f'{nome},{idade}\n')
    
arq.close()
