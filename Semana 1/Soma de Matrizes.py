'''
Exercício 2: Soma de matrizes
Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz
que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a
função deve devolver False.
'''

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

def soma_matrizes(m1,m2):
        if len(m1[0]) == len(m2[0]):
                soma_matrizes = []
                for linha1, linha2 in zip(m1, m2):
                    linha_soma = [item1 + item2 for item1, item2 in zip(linha1, linha2)]
                    soma_matrizes.append(linha_soma)
                return soma_matrizes
        else:
                return False


        
resultado = soma_matrizes(m1, m2)

if resultado is not False:
        for linha in resultado:
                print(linha)
else:
        print(False)

