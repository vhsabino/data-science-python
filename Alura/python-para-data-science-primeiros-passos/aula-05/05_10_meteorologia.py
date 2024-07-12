'''
Um instituto de meteorologia deseja fazer um estudo de temperatura 
média de cada mês do ano. Para isso, você precisa fazer um código 
que colete e armazene essas temperaturas médias em uma lista. 

Depois, calcule a média anual das temperaturas e mostre todas as 
temperaturas acima da média anual e em que mês elas ocorreram, mos-
trando os meses por extenso (Janeiro, Fevereiro, etc.).

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 11/07/2024
'''

temperatura = {'Janeiro' : 0.0, 
            'Fevereiro' : 0.0, 
            'Março' : 0.0,
            'Abril' : 0.0,
            'Maio' : 0.0,
            'Junho' : 0.0,
            'Julho' : 0.0,
            'Agosto' : 0.0,
            'Setembro' : 0.0,
            'Outubro' : 0.0,
            'Novembro': 0.0,
            'Dezembro' : 0.0}

soma = 0
for mes in temperatura.keys():
    temperatura[mes] = float(input(f'Digite a temperatura de {mes}: '))
    soma += temperatura[mes]

media = soma / 12
for mes,temp in temperatura.items():
    if temp > media:
        print(f'{mes}: {temp} graus Celsius.')
