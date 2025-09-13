import inversa

def palindromo(palabra):
    palabraInversa = inversa.inversa(palabra)
    if(palabraInversa == palabra):
        return True
    else:
        return False
