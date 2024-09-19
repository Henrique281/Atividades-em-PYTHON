# Receber a lista do usuário
entrada = input("Digite os elementos da lista separados por espaço ou vírgula: ")

# Transformar a string em uma lista de elementos
elementos = entrada.replace(",", " ").split()

# Converter os elementos para números inteiros
elementos = [int(elemento) for elemento in elementos]

# Encontrar o maior valor da lista
maior_valor = max(elementos)

# Imprimir o maior valor
print("O maior valor da lista é:", maior_valor)

# Ordenar os elementos em ordem decrescente
elementos.sort(reverse=True)

# Imprimir a lista ordenada em ordem decrescente
print("Lista em ordem decrescente:", elementos)

