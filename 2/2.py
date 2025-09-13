def mas_larga(palabras):
    mas_larga = ''
    for palabra in palabras:
        if(len(palabra) > len(mas_larga)):
            mas_larga = palabra
    return mas_larga

print(mas_larga(['cual','de','estas','palabras','es','la','mas','larga']))
