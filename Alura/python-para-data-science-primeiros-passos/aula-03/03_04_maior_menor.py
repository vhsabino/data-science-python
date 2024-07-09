'''
Escreva um programa que leia valores médios de preços de um modelo 
de carro por 3 anos consecutivos e exiba o valor mais alto e mais 
baixo entre esses três anos.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

ano_1 = float(input('digite valor do primeiro ano: '))
ano_2 = float(input('digite valor do segundo ano: '))
ano_3 = float(input('digite valor do terceiro ano: '))

if (ano_1 > ano_2) and (ano_1 > ano_3):
    print(f'valor mais alto: {ano_1}')
elif(ano_2 > ano_1) and (ano_2 > ano_3):
    print(f'valor mais alto: {ano_2}')
else:
    print(f'valor mais alto: {ano_3}')

if (ano_1 < ano_2) and (ano_1 < ano_3):
    print(f'valor mais baixo: {ano_1}')
elif(ano_2 < ano_1) and (ano_2 < ano_3):
    print(f'valor mais baixo: {ano_2}')
else:
    print(f'valor mais baixo: {ano_3}')
