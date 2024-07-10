'''
Escreva um programa que calcule o fatorial de um número inteiro 
fornecido pela pessoa usuária. Lembrando que o fatorial de um número 
inteiro é a multiplicação desse número por todos os seus antecessores 
até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

numero = int(input('digite um número: '))
fat = 1
i = numero
while i > 1:
    fat *= i
    i -= 1
print(f'{numero}! = {fat}')