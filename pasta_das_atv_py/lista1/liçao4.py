pets = [
    {"raça": "Golden Retriever", "sexo": "Fêmea", "peso": "25 kg"},
    {"raça": "Siamese", "sexo": "Macho", "peso": "4 kg"},
    {"raça": "Labrador", "sexo": "Macho", "peso": "30 kg"}
]

# Imprimir a lista original
print("Lista de animais de estimação:")
for pet in pets:
    print(pet)

# Solicitar nomes e atualizar os dicionários
for i in range(3):
    nome = input("Insira um nome para o animal de estimação {}: ".format(i+1))
    pets[i]["nome"] = nome

# Imprimir a lista atualizada
print("\nLista de animais de estimação atualizada:")
for pet in pets:
    print(pet)
