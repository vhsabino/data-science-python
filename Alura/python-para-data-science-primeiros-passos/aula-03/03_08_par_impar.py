'''
Escreva um programa que peça um número inteiro à pessoa usuária e 
determine se ele é par ou ímpar. Dica: Você pode utilizar o opera-
dor módulo %.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

numero = int(input('Digite um número inteiro: '))

if (numero % 2 == 0):
    print('é par.')
else:
    print('é impar.')