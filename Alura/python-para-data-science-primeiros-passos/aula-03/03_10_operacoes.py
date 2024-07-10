'''
Um programa deve ser escrito para ler dois números e, em seguida, 
perguntar à pessoa usuária qual operação ele deseja realizar. 
O resultado da operação deve incluir informações sobre o número 
- se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

numero_1 = float(input('digite valor do primeiro número: '))
numero_2 = float(input('digite valor do segundo número: '))

print('ESCOLHA A OPERAÇÃO')
print('1 - SOMA')
print('2 - SUBTRAÇÃO')
print('3 - MULTIPLICAÇÃO')
print('4 - DIVISÃO')
operacao = int(input())

if operacao == 1:
    resultado = numero_1 + numero_2
elif operacao == 2:
    resultado = numero_1 - numero_2
elif operacao == 3:
    resultado = numero_1 * numero_2
elif operacao == 4:
    resultado = numero_1 / numero_2
else:
    print('OPERAÇÃO INVÁLIDA')

if (operacao >= 1) and (operacao <=4):
    print(f'Resultado: {resultado}.')
    if (resultado % 2 == 0):
        print('é par.')
    else:
        print('é impar.')
    if (resultado >= 0.0):
        print('é positivo.')
    else:
        print('é negativo.')
    if (resultado - int(resultado) != 0):
        print('é decimal.')
    else:
        print('é inteiro.')