'''
Para uma seleção de produtos alimentícios, precisamos separar o 
conjunto de IDs dados por números inteiros sabendo que os produ-
tos com ID par são doces e os com ID ímpar são amargos. Monte um 
código que colete 10 IDs. Depois, calcule e mostre a quantidade 
de produtos doces e amargos.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 11/07/2024
'''

produtos = []
impares = 0
pares = 0

for i in range(1,11):
    numero = int(input('digite um ID: '))
    produtos.append(numero)

for produto in produtos:
    if (produto % 2 == 0):
        pares += 1
    else:
        impares +=1
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')