'''
Exercício 1: Gerando listas grandes
Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro
n e devolve uma lista contendo n números inteiros aleatórios.
'''
import random

def lista_grande(n):
    minimo = 1  # Valor mínimo
    maximo = n  # Valor máximo

    lista = [random.randint(minimo, maximo) for _ in range(n)]
    return lista

n = 10
lista = lista_grande(n)
print(lista)
    
