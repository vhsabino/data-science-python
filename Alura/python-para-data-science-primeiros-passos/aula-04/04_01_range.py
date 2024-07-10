'''
Escreva um programa que peça dois números inteiros e imprima 
todos os números inteiros entre eles.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

numero_1 = int(input('digite valor do primeiro número: '))
numero_2 = int(input('digite valor do segundo número: '))

if (numero_1 < numero_2):
    for i in range(numero_1,numero_2):
        if (i == numero_1):
            continue
        print(i)
elif (numero_2 < numero_1):
    for i in range(numero_2,numero_1):
        if (i == numero_2):
            continue
        print(i)
else:
    print('numeros iguais')