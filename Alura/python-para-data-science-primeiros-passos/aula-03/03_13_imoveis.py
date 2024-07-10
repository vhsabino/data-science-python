'''
Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

Para variação acima de 20%: bonificação para o time de vendas.
Para variação entre 2% e 20%: pequena bonificação para time de vendas.
Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
Para bonificações abaixo de -10%: corte de gastos.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

vendas_2022 = float(input('informe a quantidade de venda de 2022: '))
vendas_2023 = float(input('informe a quantidade de venda de 2023: '))

variacao = ((vendas_2023 - vendas_2022) / vendas_2022) * 100
if (variacao) > 20:
    print('bonificação para o time de vendas.')
elif 2 < variacao <= 20:
    print('pequena bonificação para time de vendas.')
elif -10 < variacao <= 2:
    print('planejamento de políticas de incentivo às vendas.')
else:
    print('corte de gastos.')