'''
As pessoas colaboradoras de um setor da empresa que você trabalha vão 
receber um abono correspondente a 10% do salário devido ao ótimo desem-
penho do time. O setor financeiro solicitou sua ajuda para a verifica-
ção das consequências financeiras que esse abono irá gerar nos recursos. 

Assim, foi encaminhada para você uma lista com os salários que receberão
 o abono: 

[1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. 

O abono de cada colaborador(a) não pode ser inferior a 200. Em código, 
transforme cada um dos salários em chaves de um dicionário e o abono de 
cada salário no elemento. Depois, informe o total de gastos com o abono, 
quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior va-
lor de abono fornecido.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 11/07/2024
'''

abonos = {1172.0: 0.0,
          1644.0: 0.0,
          2617.0: 0.0,
          5130.0: 0.0,
          5532.0: 0.0,
          6341.0: 0.0,
          6650.0: 0.0,
          7238.0: 0.0,
          7685.0: 0.0,
          7782.0: 0.0,
          7903.0: 0.0}

minimo = 0
total = 0
maior = 0
for salario,abono in abonos.items():
    abono = salario * 0.10
    if abono < 200:
        abono = 200
        minimo += 1
    total += abono
    abonos[salario] = abono
    if abono > maior:
        maior = abono
print(f'Total de gastos com abono: {total}')
print(f'Colaboradores q receberam o mínimo: {minimo}')
print(f'Maior valor de abono fornecido: {maior}')

