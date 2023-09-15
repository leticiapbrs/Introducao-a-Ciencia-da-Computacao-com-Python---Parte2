def primeiro_lex(lista):
    if len(lista) == 0:
        return None

    primeiro = lista[0]

    for palavra in lista:
        if palavra < primeiro:
            primeiro = palavra

    return primeiro
