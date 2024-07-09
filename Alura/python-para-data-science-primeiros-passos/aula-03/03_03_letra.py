'''
Escreva um programa que determine se uma letra fornecida pela pessoa usuária 
é uma vogal ou consoante.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

letra = str(input('digite uma letra: '))

if ((letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u')):
    print('vogal')
else:
    print('consoante')