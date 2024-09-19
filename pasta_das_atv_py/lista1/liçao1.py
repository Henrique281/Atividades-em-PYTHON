import random

Pessoa = {
    "idade": random.randint(18,80),
    "sexo": random.choice(["Masculino","feminino"]),
    "peso": round(random.uniform(50, 100), 2),
    "altura": round(random.uniform(1.5, 2.0), 2)
}

print(Pessoa)

povoado = [Pessoa] * 500
print (povoado)