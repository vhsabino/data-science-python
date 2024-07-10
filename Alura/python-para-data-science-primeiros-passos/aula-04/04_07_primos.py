'''
Os números primos possuem várias aplicações dentro da Ciência de Dados 
em criptografia e segurança, por exemplo. Um número primo é aquele que 
é divisível apenas por um e por ele mesmo. Assim, faça um programa que 
peça um número inteiro e determine se ele é ou não um número primo.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

numero = int(input('digite um número: '))

i = numero - 1
count = 0

while i > 1:
    if numero % i == 0:
        count += 1
    i -= 1
if count > 0:
    print('nao eh primo')
else:
    print('eh primo')