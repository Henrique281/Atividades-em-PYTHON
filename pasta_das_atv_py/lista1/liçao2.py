import math

def calcula_triangulo(c1, c2):
    hipotenusa = math.sqrt(c1**2 + c2**2)
    area = (c1 * c2) / 2
    return hipotenusa, area

# Teste da função
x = calcula_triangulo(8, 6)
print(f'Hipotenusa: {x[0]}')
print(f'Área: {x[1]}')
