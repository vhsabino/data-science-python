'''
Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. 
Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação 
de qual é o Estado a que pertence: 

estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG'].

A empresa sempre está abrindo novas filiais, de modo que a tabela está constantemente 
recebendo novos registros e o gestor gostaria de possuir a informação atualizada da 
quantidade de filiais em cada Estado.

A partir da coluna com a informação dos Estados, crie um dicionário usando dict 
comprehension com a chave sendo o nome de um Estado e o valor sendo a contagem de 
vezes em que o Estado aparece na lista.

Dica: Você pode fazer um passo intermediário para gerar uma lista de listas em que 
cada uma das listas possui o nome de apenas um Estado com valores repetidos.

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 17/07/2024
'''

estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

estados_com_filiais = list(set(estados))
n_filiais = []
for i in range(len(estados_com_filiais)):
    n = 0
    for estado in estados:
        if estado == estados_com_filiais[i]:
            n += 1
    n_filiais.append(n)
filiais = {estados_com_filiais[i]:n_filiais[i] for i in range(len(estados_com_filiais))}
print(filiais)