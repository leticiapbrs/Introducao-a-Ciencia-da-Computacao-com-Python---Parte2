def busca(lista, numero):
    for i, elemento in enumerate(lista):
        if elemento == numero:
            return i
    return False
