'''
Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 13/07/2024
'''

from random import choice

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
numero = choice(lista)
print(numero)