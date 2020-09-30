from tqdm import tqdm
from time import sleep
import math
def menu():
    opcao = 'sim'
    while opcao == 'sim':
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
def novamente():
        opcao = str(input('gostaria de fazer mais alguma taboada?: '))
        if opcao == 'não' or novamente == 'nao':
            print('good bye')
            exit()
        else:
            print('opção invalida!')
            return novamente()
menu();
novamente();
exit()
