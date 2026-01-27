arq = open('teste.txt', 'w')

for i in range(4):
    palavra = input('Palavra: ')
    arq.write(palavra)
    arq.write('\n')

arq.close()
