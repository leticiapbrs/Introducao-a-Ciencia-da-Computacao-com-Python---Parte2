def soma_lista(lista):
    soma = 0
    for numero in lista:
        if isinstance(numero, int):
            soma += numero
    return soma
    

lista = [1,2,3,4,5]
resultado = soma_lista(lista)
print(resultado)
        
        
