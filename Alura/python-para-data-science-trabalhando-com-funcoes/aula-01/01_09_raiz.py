'''
Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identifi-
cando quais resultaram em um número inteiro. A lista é a seguinte:

numeros = [2, 8, 15, 23, 91, 112, 256]

No final, informe quais números possuem raízes inteiras e seus respectivos valores.

Dica: use a comparação entre a divisão inteira (//) da raiz por 1 com o valor da raiz 
para verificar se o número é inteiro. Por exemplo:

num = 1.5
num_2 = 2
print(f'{num} é inteiro? :', num // 1 == num)
print(f'{num_2} é inteiro? :', num_2 // 1 == num_2)

Saída:

1.5 é inteiro? : False
2 é inteiro? : True

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 13/07/2024
'''

from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]

print("Possuem raízes inteiras: ")
for n in numeros:
    raiz = sqrt(n)
    if (raiz // 1 == raiz):
        print(f"{n} => {raiz}")
