'''
Faça um código que colete em uma lista 5 números inteiros quaisquer 
e imprima a lista. Exemplo: [1,4,7,2,4].

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 10/07/2024
'''

lista = []
for i in range(0,5):
    numero = int(input('digite um número: '))
    lista.append(numero)
print(lista)