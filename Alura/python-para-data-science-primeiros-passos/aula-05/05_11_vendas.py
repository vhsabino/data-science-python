'''
Uma empresa de e-commerce está interessada em analisar as vendas dos 
seus produtos. Os dados das vendas foram armazenados em um dicionário:

{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 11/07/2024
'''

vendas = {'Produto A': 300, 
          'Produto B': 80, 
          'Produto C': 60,
          'Produto D': 200, 
          'Produto E': 250, 
          'Produto F': 30}

total = 0
maior_valor = 0
maior_produto = ''
for produto,valor in vendas.items():
    total += valor
    if valor > maior_valor:
        maior_produto = produto
        maior_valor = valor
print(f'Total de vendas: {total}')
print(f'Produto mais vendido: {maior_produto}')

