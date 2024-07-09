'''
Escreva um programa que pergunte sobre o preço de três produtos 
e indique qual é o produto mais barato para comprar.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

produto_1 = float(input('digite valor do primeiro produto: '))
produto_2 = float(input('digite valor do segundo produto: '))
produto_3 = float(input('digite valor do terceiro produto: '))

if (produto_1 < produto_2) and (produto_1 < produto_3):
    print(f'valor mais baixo: produto 1')
elif(produto_2 < produto_1) and (produto_2 < produto_3):
    print(f'mais barato: produto 2')
else:
    print(f'valor mais baixo: produto 3')