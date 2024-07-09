'''
Crie um programa que solicite dois valores numéricos,
um numerador e um denominador e realize a divisão in-
teira entre os dois valores. Deixe claro que o valor 
do denominador não pode ser 0.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 08/07/2024
'''

numero_1 = int(input('Digite o numerador: '))
numero_2 = int(input('Digite o denominador(Não pode ser ZERO!): '))
divisao_inteira = numero_1 // numero_2
print(divisao_inteira)