#!/usr/bin/env python
import math
print('=============================================')
print('=====                                        =====')
print('=====        Bem vindo a calculadora         =====')
print('=====                de tabuada              =====')
print('=====                                        =====')
print('=============================================')
def menu():
    numIn = input('digite um numero de 1 a 9: ')
    contador = 1
    if numIn == "":
        print('não é um número valido para uma tabuada')
        return menu()
    num = int(numIn)
    if num != 0 and num <= 10:
        while contador != 11:
            resultado = num * contador
            print(str(num) + ' X ' + str(contador) + ' = ' + str(resultado))
            contador = contador + 1
    if num <= 0 or num > 10 or num == "":
        print('não é um número valido para uma tabuada')
        return menu()
    opcao = str(input('gostaria de fazer mais alguma tabuada?: '))
    if opcao == 'não' or opcao == 'nao':
        print('good bye')
        exit()
    if opcao == 'sim' or opcao == 'Sim' or opcao == " sim" or opcao == " Sim" or opcao == "sim " or opcao == "Sim ":
        return menu()
    if opcao != 'sim' and opcao != 'nao' and opcao != 'não':
        print('opção invalida!.... saindo do programa por inserção de dados inválidos')
        exit()
    elif opcao == "":
        print('opção invalida!.... saindo do programa por inserção de dados inválidos')
        exit()
menu();
