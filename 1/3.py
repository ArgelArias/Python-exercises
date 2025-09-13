def myLen(cadena):
    contador = 0
    for letra in cadena:
        contador += 1
    return contador

cadena = "cadena"
print("La cadena 'cadena' tiene una longitud de", myLen(cadena))
