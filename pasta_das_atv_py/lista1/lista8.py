import math

def calcula_bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return None  # Não existem raízes reais
    
    raiz_delta = math.sqrt(delta)
    
    x1 = (-b + raiz_delta) / (2*a)
    x2 = (-b - raiz_delta) / (2*a)
    
    return x1, x2

# Teste da função
x = calcula_bhaskara(1, 4, 1)
print(f'x1 = {x[0]}')
print(f'x2 = {x[1]}')
