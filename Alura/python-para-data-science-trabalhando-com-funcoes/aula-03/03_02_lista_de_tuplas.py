'''
Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla conti-
da na seguinte lista de tuplas:

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 15/07/2024
'''

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

nova_lista = [elemento[2] for elemento in lista_de_tuplas]

print(nova_lista)