def dividir_lista(original, n):
    # 'n' é o número de elementos que irão para a primeira lista
    primeira_parte = original[:n]
    segunda_parte = original[n:]
    return primeira_parte, segunda_parte

# Exemplo de uso
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primeira, segunda = dividir_lista(lista_original, 4)

print("Primeira parte:", primeira)
print("Segunda parte:", segunda)