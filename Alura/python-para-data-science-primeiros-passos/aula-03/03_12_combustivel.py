'''
Um estabelecimento está vendendo combustíveis com descontos variados. 
Para o etanol, se a quantidade comprada for até 15 litros, o desconto 
será de 2% por litro. Caso contrário, será de 4% por litro. Para o die-
sel, se a quantidade comprada for até 15 litros, o desconto será de 3% 
por litro. Caso contrário, será de 5% por litro. O preço do litro de 
diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um pro-
grama que leia a quantidade de litros vendidos e o tipo de combustível 
(E para etanol e D para diesel) e calcule o valor a ser pago pelo clien-
te. Tenha em mente algumas dicas:

O do valor do desconto será a multiplicação entre preço do litro, quan-
tidade de litros e o valor do desconto.
O valor a ser pago por um cliente será o resultado da multiplicação do 
preço do litro pela quantidade de litros menos o valor de desconto resul-
tante do cálculo.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

litros = float(input('qts litros foram vendidos? '))
tipo = str(input('ql o tipo d combustível? '))

if (tipo.upper() == 'D'):
    if (litros <= 15.0):
        valor = 2.0 * litros * 0.97
    else:
        valor = 2.0 * litros * 0.95
    print(f'Valor a pagar: R$ {valor}')
elif (tipo.upper() == 'E'):
    if (litros <= 15.0):
        valor = 1.7 * litros * 0.98
    else:
        valor = 1.7 * litros * 0.96
    print(f'Valor a pagar: R$ {valor}')
else:
    print('tipo d combustível inválido!')