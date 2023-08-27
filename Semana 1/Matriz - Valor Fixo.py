def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
            '''O método append() é"
            utilizado para adicionar um elemento ao final da lista existente.'''

        matriz.append(linha)
    return matriz

matriz_resultante = cria_matriz(3,3,0)
for linha in matriz_resultante:
    print(linha)
    
