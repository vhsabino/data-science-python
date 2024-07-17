'''
Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade 
de pessoas colaboradoras e o(a) gestor(a) gostaria de ter um agrupamento da soma dessas 
pessoas para cada estado. As informações contidas na tabela são:

funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

A partir da lista de tuplas, crie um dicionário em que as chaves são os nomes dos Estados 
únicos e os valores são as listas com o número de colaboradores(as) referentes ao Estado. 
Crie também um dicionário em que as chaves são os nomes dos Estados e os valores são a 
soma de colaboradores(as) por Estado.

Dica: Você pode fazer um passo intermediário para gerar uma lista de listas em que cada 
uma das listas possui apenas os valores numéricos de funcionários(as) de cada Estado.

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 17/07/2024
'''

funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

estados = [estado[0] for estado in funcionarios]
estados_com_funcionarios = list(set(estados))
n_funcionarios = []
for i in range(len(estados_com_funcionarios)):
    list_funcionarios = [estado[1] for estado in funcionarios if estado[0] == estados_com_funcionarios[i]]
    n_funcionarios.append(list_funcionarios)

colaboradores = {estados_com_funcionarios[i]:n_funcionarios[i] for i in range(len(estados_com_funcionarios))}
print(colaboradores)
colaboradores_total = {estados_com_funcionarios[i]:sum(n_funcionarios[i]) for i in range(len(estados_com_funcionarios))}
print(colaboradores_total)
