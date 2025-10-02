def verificar_par(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False


## PROGRAMA PRINCIPAL
    
num = int(input('Digite um número: '))
if verificar_par(num) == True:
    print('é par')
else:
    print('não é par')
