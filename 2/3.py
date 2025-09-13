def filtrar_palabras(palabras, num):
    final = []
    for palabra in palabras:
        if(len(palabra) > num):
            final.append(palabra)
    return final

print(filtrar_palabras(['cual','de','estas','palabras','es','la','mas','larga'], 3))
