'''
Você está trabalhando com processamento de linguagem natural (NLP) e, dessa vez, sua 
líder requisitou que você criasse um trecho de código que recebe uma lista com as pa-
lavras separadas de uma frase gerada pelo ChatGPT.

Você precisa criar uma função que avalia cada palavra desse texto e verificar se o 
tratamento para retirar os símbolos de pontuação (',' '.', '!' e '?') foi realizado. 
Caso contrário, será lançada uma exceção do tipo ValueError apontando o 1º caso em 
que foi detectado o uso de uma pontuação por meio da frase "O texto apresenta pontua-
ções na palavra "[palavra]".". Essa demanda é voltada para a análise do padrão de fra-
ses geradas pela inteligência artificial.

Dica: Para verificar se uma ou mais das pontuações estão presentes em cada palavra, 
utilize a palavra chave or na condição if. Por exemplo, 'a' in 'alura' or 'b' in 
'alura'… Saída: True

Os dados para o teste do código são:

Lista tratada:

lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

Lista não tratada:

lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 21/07/2024
'''

def verificacao(lista: list):
    try:
        for elemento in lista:
            if (',' in elemento or '.' in elemento or '!'  in elemento or '?' in elemento):
                raise ValueError(f"O texto apresenta pontuações na palavra {elemento}.")
        resultado = True
    except Exception as e:
        print(e)
        resultado = False
    return resultado


lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

resultado_1 = verificacao(lista_tratada)
print(resultado_1)

resultado_2 = verificacao(lista_nao_tratada)
print(resultado_2)


