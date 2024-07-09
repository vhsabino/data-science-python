'''
Escreva um programa que peça à pessoa usuária para fornecer 
dois números e exibir o número maior.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

numero_1 = int(input('digite o primeiro número: '))
numero_2 = int(input('digite o segundo número: '))

if (numero_1 > numero_2):
    print(f'maior número: {numero_1}')
else:
    print(f'maior número: {numero_2}')