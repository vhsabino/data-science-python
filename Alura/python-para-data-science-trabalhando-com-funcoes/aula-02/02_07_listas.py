'''
Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as 
para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

O texto exibido ao fim deve ser parecido com:

"Nome completo: Ana Silva"

Dica: utilize a função map para mapear os nomes e sobrenomes e as funções de string para tratar o texto.

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 14/07/2024
'''

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nome_completo = map(lambda x,y: x.lower().capitalize() + " " + y.lower().capitalize(), nomes, sobrenomes)

for nome in nome_completo:
    print(f"Nome completo: {nome}")