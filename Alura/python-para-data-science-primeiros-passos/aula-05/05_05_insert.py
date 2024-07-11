'''
Faça um programa que, ao inserir um número qualquer, cria uma lista 
contendo todos os números primos entre 1 e o número digitado.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 10/07/2024
'''

numero = int(input('digite um número: '))

for i in range (2,numero):
    j = i - 1
    count = 0
    while j > 1:
        if i % j == 0:
            count += 1
        j -= 1
    if count == 0:
        print(i)
