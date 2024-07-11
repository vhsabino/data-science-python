'''
Colete novamente 5 inteiros e imprima a lista em ordem inversa à 
enviada.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 10/07/2024
'''

lista = []
for i in range(0,5):
    numero = int(input('digite um número: '))
    lista.append(numero)

for i in range(0,5):
    print(lista.pop())