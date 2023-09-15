'''
Exercício 2: Triângulos semelhantes
Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe
um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é
semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve ]
devolver True. Caso negativo, deve devolver False

Um triângulo é semelhante a outro triângulo se a razão (divisão) entre os comprimentos
dos seus lados forem iguais.

Dica: você pode colocar os lados de cada um dos triângulos em uma lista diferente e
ordená-las.
'''


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lados = [lado1, lado2, lado3]
        self.lados.sort()  
    def semelhantes(self, outro_triangulo):
        outro_lados = outro_triangulo.lados
        outro_lados.sort()  

        # Verifica se as razões entre os lados são iguais (semelhantes)
        razoes_atuais = [self.lados[0] / outro_lados[0], self.lados[1] / outro_lados[1], self.lados[2] / outro_lados[2]]
        
        # Se todas as razões forem iguais, os triângulos são semelhantes
        if razoes_atuais[0] == razoes_atuais[1] == razoes_atuais[2]:
            return True
        else:
            return False

# Exemplo de uso:
triangulo1 = Triangulo(6, 8, 10)
triangulo2 = Triangulo(3, 4, 5)

if triangulo1.semelhantes(triangulo2):
    print("Os triângulos são semelhantes.")
else:
    print("Os triângulos não são semelhantes.")
