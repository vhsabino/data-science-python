'''
Com os mesmos dados da questão anterior, defina quantas compras foram 
realizadas acima de 3000 reais e calcule a porcentagem quanto ao total 
de compras.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 10/07/2024
'''

lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

qtd = 0

for elemento in lista:
    if elemento > 3000:
        qtd += 1
print(f'{(qtd / len(lista)) * 100}%')