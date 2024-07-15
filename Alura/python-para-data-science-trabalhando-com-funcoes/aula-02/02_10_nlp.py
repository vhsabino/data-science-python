'''
Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). 
Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pes-
soa usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. 
Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de pala-
vras acima dessa quantidade de caracteres.

Dica: utilize as funções lambda e filter() para filtrar essas palavras. Lembrando que a função 
embutida filter() recebe uma função (no nosso exemplo uma função lambda) e filtra um iterável 
de acordo com a função. Para tratar a frase use replace() para trocar a ',' '.', '!' e '?' por 
espaço.

Use a frase "Aprender Python aqui na Alura é muito bom" para testar o código.

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 14/07/2024
'''


frase = "Aprender Python aqui na Alura é muito bom"
frase = frase.replace(","," ").replace("."," ").replace("!"," ").replace("?"," ")
palavras = frase.split()

frase_tratada = list(filter(lambda x: len(x) >= 5, palavras))

print(frase_tratada)
