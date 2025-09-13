def generar_n_caracteres(num, car):
    final = ''
    for i in range(num):
        final += car
    return final

print(generar_n_caracteres(5,'x'))
