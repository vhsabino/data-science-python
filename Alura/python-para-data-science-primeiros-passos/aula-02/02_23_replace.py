'''
Crie um código que solicite uma frase à pessoa usuária e imprima 
a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 08/07/2024
'''

frase = str(input('Digite uma frase: ')).replace('s','$')
print(frase)