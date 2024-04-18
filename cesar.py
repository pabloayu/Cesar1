alfabeto = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def cifrar(frase, distancia):
    result = ""
    for letra in frase.upper():
        if letra in alfabeto:
            new_letra = alfabeto[(alfabeto.index(letra) + distancia) % len(alfabeto)]
        else:
            new_letra = letra
        result += new_letra
    return result