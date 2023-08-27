def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

num_linhas = int(input("Digite o número de linhas da matriz: "))
num_colunas = int(input("Digite o número de colunas da matriz: "))
matriz_resultante = cria_matriz(num_linhas, num_colunas)

for linha in matriz_resultante:
    print(linha)
