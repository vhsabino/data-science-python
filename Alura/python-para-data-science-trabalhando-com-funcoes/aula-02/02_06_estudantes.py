'''
Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de 
seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e 
retorne:

- maior nota
- menor nota
- média
- situação (Aprovado(a) ou Reprovado(a))

Para testar o comportamento da função, os dados podem ser exibidos em um texto:

"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e 
a menor nota de [menor] pontos e foi [situacao]"

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 14/07/2024
'''

def analise(lista: list):
    maior_nota = max(lista)
    menor_nota = min(lista)
    media = sum(lista) / len(lista)
    if media >= 7.0:
        situacao_aluno = "Aprovado(a)"
    else:
        situacao_aluno = "Reprovado(a)"
    return media,maior_nota,menor_nota,situacao_aluno

lista = [5.0, 6.5, 8.5, 9.5]
media,maior,menor,situacao = analise(lista)

print(f"O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}")