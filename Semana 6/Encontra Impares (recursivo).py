'''
Exercício 2: Encontrando ímpares em uma lista
Implemente a função encontra_impares(lista), que recebe como parâmetro uma
lista de números inteiros e devolve uma outra lista apenas com os números
ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem.
'''

def encontra_impares(lista):
    if not lista:
        return []
    else:
        primeiro_numero = lista[0]
        restante_da_lista = lista[1:]
        if isinstance(primeiro_numero, int) and primeiro_numero % 2 == 1:
            return [primeiro_numero] + encontra_impares(restante_da_lista)
        else:
            return encontra_impares(restante_da_lista)
