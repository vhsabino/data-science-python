'''
Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 13/07/2024
'''

from math import pow

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
expoente = 2

quadrado = map(lambda x: pow(x,expoente),lista)
lista_quadrado = list(quadrado)
print(lista_quadrado)
