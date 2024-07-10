'''
Escreva um programa para calcular quantos dias levará para a colônia de 
uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com 
base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere 
que a colônia A inicia com 4 elementos e a B com 10.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

n_a = 4
n_b = 10
dias = 0
while n_a <= n_b:
    n_a *= 1.03
    n_b *= 1.015
    dias += 1
print(f'{dias} dias.')