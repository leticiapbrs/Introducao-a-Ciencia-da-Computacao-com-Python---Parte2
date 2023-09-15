'''
Exercício 1: Contando vogais ou consoantes
Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro
parâmetro uma string contendo uma frase e como segundo parâmetro uma outra
string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver o
numero de vogais presentes na frase. Quando ele for definido como "consoantes",
a função deve devolver o número de consoantes presentes na frase. Se este
parâmetro não for passado para a função, deve-se assumir o valor "vogais" para oparâmetro.
'''

frase = "Programas em Python"

def conta_letras(frase,contar="vogais"):
    frase = frase.lower()
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"

    if contar == "vogais":
        contador = sum(1 for letra in frase if letra in vogais)
    elif contar == "consoantes":
        contador = sum(1 for letra in frase if letra in consoantes)
    else:
        contador = 0
                    
    return contador

if conta_letras(frase, contar="vogais"):
    resultado_vogais = conta_letras(frase, contar="vogais")
    print(resultado_vogais)
elif conta_letras(frase, contar="consoantes"):
    resultado_consoantes = conta_letras(frase, contar="consoantes")
    print(resultado_consoantes)
            
