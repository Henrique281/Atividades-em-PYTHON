# Receber a lista do usuário
entrada = input("Digite os elementos da lista separados por espaço ou vírgula: ")

# Transformar a string em uma lista de elementos
elementos = entrada.replace(",", " ").split()

# Converter os elementos para números inteiros
elementos = [int(elemento) for elemento in elementos]

# Encontrar o maior valor da lista
soma_valor = sum(elementos)

# Imprimir o maior valor
print("A soma de todos os numeros é:", soma_valor)

# Ordenar os elementos em ordem crescente
elementos.sort()

# Imprimir a lista ordenada em ordem crescente
print("Lista em ordem crescente:", elementos)