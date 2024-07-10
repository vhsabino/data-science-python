'''
Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, 
de acordo com a escolha da pessoa usuária. Como exemplo, para o número 
2, a tabuada deve ser mostrada no seguinte formato:

Tabuada do 2:
2 x 1 = 2
2 x 2 = 4
[...]
2 x 10 = 20

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

numero = int(input('digite um número: '))

print(f'Tabuada do {numero}')
for i in range (1,11):
    print(f'{numero} x {i} = {numero*i}')