'''
Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada 
tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), 
('Apartamento', 1900), ('Casa', 1100)]

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 15/07/2024
'''

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

nova_lista = [elemento[1] for elemento in aluguel if elemento[0] == 'Apartamento']

print(nova_lista)