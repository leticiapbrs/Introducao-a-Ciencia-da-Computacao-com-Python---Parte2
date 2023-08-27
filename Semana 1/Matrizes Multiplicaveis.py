m1 = [[1], [4], [2]]
m2 = [[2, 3, 4]]

def sao_multiplicaveis(m1,m2):
        if len(m1[0]) == len(m2):
                return True
        else:
                return False


        
resultado = sao_multiplicaveis(m1, m2)

if resultado is True:
        print(True)
else:
        print(False)

