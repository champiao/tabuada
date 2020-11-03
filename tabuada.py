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
    if num <= 0 or num > 10:
        print('nao e um numero valido para uma taboada')
        return menu()
    opcao = str(input('gostaria de fazer mais alguma taboada?: '))
    if opcao == 'não' or opcao == 'nao':
        print('good bye')
        exit()
    if opcao == 'sim':
        return menu()
    if opcao != 'sim' and opcao != 'nao' and opcao != 'não':
        print('opção invalida!.... saindo do programa por inserção de dados inválidos')
menu();
