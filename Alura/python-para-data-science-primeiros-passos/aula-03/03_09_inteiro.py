'''
Escreva um programa que peça um número à pessoa usuária e 
informe se ele é inteiro ou decimal.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

numero = float(input('Digite um número: '))

if (numero - int(numero) != 0):
    print('é decimal.')
else:
    print('é inteiro.')