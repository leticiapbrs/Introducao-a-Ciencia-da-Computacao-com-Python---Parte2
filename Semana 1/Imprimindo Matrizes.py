minha_matriz = [[1,2], [2,9], [3,9]]

def imprime_matriz(minha_matriz):
    for lista in minha_matriz:
        for numero in lista:
            print(numero, end=" ")
            if numero < len(lista) - 1:
                print(" ", end="")
        print()  # Adiciona uma quebra de linha após cada lista
    return imprime_matriz

imprime_matriz(minha_matriz)

print()
