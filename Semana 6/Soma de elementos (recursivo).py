'''
Exercício 1: Soma dos elementos de uma lista
Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de
números inteiros e devolve um número inteiro correspondente à soma dos
elementos desta lista.

Sua solução deve ser implementada utilizando recursão.
'''

def soma_lista(lista):
    if not lista:
        return 0  
    else:
        return lista[0] + soma_lista(lista[1:])  


lista = [1, 2, 3, 4, 5]
resultado = soma_lista(lista)
print(resultado) 
