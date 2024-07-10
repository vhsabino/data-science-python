'''
Vamos entender a distribuição de idades de pensionistas 
de uma empresa de previdência. Escreva um programa que 
leia as idades de uma quantidade não informada de clientes 
e mostre a distribuição em intervalos de [0-25], [26-50], 
[51-75] e [76-100]. Encerre a entrada de dados com um nú-
mero negativo.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

range_1 = 0
range_2 = 0
range_3 = 0
range_4 = 0

while True:
    idade = int(input('digite uma idade: '))
    if idade < 0:
        break
    else:
        if (idade >= 0) and (idade <= 25):
            range_1 += 1
        elif (idade > 25) and (idade <= 50):
            range_2 += 1
        elif (idade > 50) and (idade <= 75):
            range_3 += 1
        elif (idade > 75) and (idade <= 100):
            range_4 += 1
        else:
            print('acima de 100 anos lol')
print(f'[0-25]: {range_1}')
print(f'[26-50]: {range_2}')
print(f'[51-75]: {range_3}')
print(f'[76-100]: {range_4}')