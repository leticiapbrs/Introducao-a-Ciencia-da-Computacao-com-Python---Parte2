'''
Exercício 2: Ordem lexicográfica
Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista)
que recebe uma lista de strings como parâmetro e devolve o primeiro string na
ordem lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas.
'''

lista = ['oĺá', 'A', 'a', 'casa']


def primeiro_lex(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

primeiro = primeiro_lex(lista)
print(primeiro[0])
