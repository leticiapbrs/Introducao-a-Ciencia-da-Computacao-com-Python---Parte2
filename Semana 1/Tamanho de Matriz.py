'''
Exercício 1: Tamanho da matriz
Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e
imprime as dimensões da matriz recebida, no formato iXj.
'''

def dimensoes(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0]) if matriz else 0  # Verifica o número de colunas da primeira linha
    
    print(f"{num_linhas}X{num_colunas}")

# Exemplo de uso
minha_matriz = [[1, 2, 3, 6], [4, 5, 6, 6]]
dimensoes(minha_matriz)
