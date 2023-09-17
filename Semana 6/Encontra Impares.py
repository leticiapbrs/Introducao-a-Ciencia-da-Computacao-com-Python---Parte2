def encontra_impares(lista):
    impares = []
    for numero in lista:
        if isinstance(numero, int) and numero%2 == 1:
            impares.append(numero)
        else:
            return 0
    return impares
    

lista = [1,2,3,4,5]
resultado = encontra_impares(lista)
print(resultado)
        
        
