'''
Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular 
a potência do 1º número elevado ao 2º.

Dica: use a função pow() da biblioteca math

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 13/07/2024
'''

import math

numero_1 = int(input('digite o primeiro numero: '))
numero_2 = int(input('digite o segundo numero: '))

print(f"{numero_1}^{numero_2} = {pow(numero_1,numero_2)}")