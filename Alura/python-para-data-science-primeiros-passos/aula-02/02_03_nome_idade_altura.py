'''
Crie um programa que solicite à pessoa usuária digitar 
seu nome, idade e altura em metros, e imprima “Olá, 
[nome], você tem [idade] anos e mede [altura] metros!”.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 08/07/2024
'''

nome = input('ql o seu nome? ')
idade = int(input('ql a sua idade? '))
altura = float(input('ql a sua altura? '))
print(f'Olá, {nome}, você tem {idade} anos e mede {altura} metros!.')