'''
A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para 
gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do 
nome na lista original e o segundo elemento sendo o próprio nome.

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 15/07/2024
'''

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

lista_tuplas = [(i, lista[i]) for i in range(len(lista))]
print(lista_tuplas)