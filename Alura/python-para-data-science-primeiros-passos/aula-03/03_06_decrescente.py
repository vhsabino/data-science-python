'''
Escreva um programa que leia três números e os exiba em ordem decrescente.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

numero_1 = int(input('digite valor do primeiro produto: '))
numero_2 = int(input('digite valor do segundo produto: '))
numero_3 = int(input('digite valor do terceiro produto: '))

if (numero_1 > numero_2) and (numero_1 > numero_3):
    print(numero_1)
    if (numero_2 > numero_3):
        print(numero_2)
        print(numero_3)
    else:
        print(numero_3)
        print(numero_2)
elif(numero_2 > numero_1) and (numero_2 > numero_3):
    print(numero_2)
    if (numero_1 > numero_3):
        print(numero_1)
        print(numero_3)
    else:
        print(numero_3)
        print(numero_1)
else:
    print(numero_3)
    if (numero_2 > numero_1):
        print(numero_2)
        print(numero_1)
    else:
        print(numero_1)
        print(numero_2)