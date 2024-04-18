def cifrar(frase, distancia):
    alfabeto = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    cadena_cifrada = ""
    frase = frase.upper()
    for letra in frase:
        if letra in alfabeto:
            posicion_inicial = alfabeto.index(letra)
            nueva_posicion = posicion_inicial + distancia
            while nueva_posicion >= len(alfabeto):
                nueva_posicion -= len(alfabeto)
            cadena_cifrada += alfabeto[nueva_posicion]
        else:
            # Si el caracter no es una letra, lo añadimos sin cifrar
            cadena_cifrada += letra
    return cadena_cifrada

# Ejemplo de uso:
frase = "HOLA MUNDO"
distancia = 1
print("Frase original:", frase)
print("Frase cifrada:", cifrar(frase, distancia))
