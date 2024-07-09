'''
Crie um código que solicite uma frase à pessoa usuária e imprima 
a mesma frase sem espaços em branco no início e no fim e em le-
tras minúsculas.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 08/07/2024
'''

frase = str(input('Digite uma frase: ')).strip().lower()
print(frase)