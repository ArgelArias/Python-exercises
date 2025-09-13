def inversa(cadena):
    inversa = ""
    indice = len(cadena)
    while indice:
        inversa += cadena[indice-1]
        indice -= 1
    return inversa

print(inversa('Hola'))
