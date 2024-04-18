abecedario = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZA")
abecedario1 = list("abcdefghijklmnñopqrstuvwxyza")

def cifrar(frase, distancia):
    retorno = ""
    for i in frase:
        if i in abecedario:
            n = abecedario.index(i)
            retorno += abecedario[(n + distancia) % len(abecedario)]
        elif i in abecedario1:
            n = abecedario1.index(i)
            retorno += abecedario1[(n + distancia) % len(abecedario1)]
        else:
            retorno += i  # Para manejar caracteres que no están en las listas, como espacios o signos de puntuación.
    return retorno

print(cifrar("Hola", 1))
print(cifrar("Pablo", 2))