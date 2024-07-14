'''
Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma em-
presa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita 
à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.

"Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 13/07/2024
'''

from random import randrange

nome = str(input("Qual o seu nome? "))
token = randrange(1000,9998)

print(f'Olá, {nome}, o seu token de acesso é {token}! Seja bem vindo(a)!')