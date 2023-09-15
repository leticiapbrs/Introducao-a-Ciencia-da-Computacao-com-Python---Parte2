def menor_nome(nomes):
    menor = None  

    for nome in nomes:
        nome = nome.strip()  
        if menor is None or len(nome) < len(menor):
            menor = nome

    if menor is not None:
        return menor.capitalize()  
    else:
        return None  


nomes = ['LU   ', ' josé ', 'PAULO', 'Catarina']
resultado = menor_nome(nomes)
print(resultado)  
