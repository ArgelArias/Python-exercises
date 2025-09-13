def NumMasPopular(numeros, tamano):
    dict = {}
    for i in range(0,tamano):
        if numeros[i] not in dict:
            dict[numeros[i]] =1
        else:
            dict[numeros] += 1
    print(dict)

print(NumMasPopular([1,2,3,4,5],5))
print('Se me termino el tiempo :(')
