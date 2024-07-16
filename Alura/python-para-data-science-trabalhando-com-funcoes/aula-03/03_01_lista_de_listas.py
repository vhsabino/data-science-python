'''
Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na se-
guinte lista:

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 15/07/2024
'''

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

soma = [sum(elemento) for elemento in lista_de_listas]

print(soma)