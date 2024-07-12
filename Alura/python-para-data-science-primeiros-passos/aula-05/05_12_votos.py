'''
Uma pesquisa de mercado foi feita para decidir qual design de marca infantil 
mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser 
observados abaixo:

Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos

Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, 
informe o design vencedor e a porcentagem de votos recebidos.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 11/07/2024
'''

votacao = {'Design 1': 1334, 
          'Design 2': 982, 
          'Design 3': 1751,
          'Design 4': 210, 
          'Design 5': 1811}

total = 0
maior_voto = 0
maior_design = ''
for design,votos in votacao.items():
    total += votos
    if votos > maior_voto:
        maior_design = design
        maior_voto = votos
print(f'Design vencedor: {maior_design} : {(maior_voto / total) * 100}% dos votos')