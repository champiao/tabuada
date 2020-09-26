from tqdm import tqdm
from time import sleep
import math
def menu():
    num = int(input('digite um numero de 1 a 9: '))
    contador = 1
    if num != 0 and num <= 10:
        while contador != 11:
            resultado = num * contador
            print(str(num) + ' X ' + str(contador) + ' = ' + str(resultado))
            contador = contador + 1
    else:
        print('nao e um numero valido para uma taboada')
        return menu()
def NovoCalculo():
    novamente = str(input('gostaria de fazer mais alguma taboada?: '))
    if novamente == 'sim':
        return menu()
    if novamente == 'não' or novamente == 'nao':
        print('good bye')
        exit()
    else:
        print('opção invalida!')
        return NovoCalculo()
menu();
NovoCalculo();
exit()
