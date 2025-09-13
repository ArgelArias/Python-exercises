import re

def mayus(cadena):
    res = re.findall("[A-Z]", cadena)
    return len(res)

entrada = input('Inserte una cadena\n')

print('Tu cadena tiene : ' + str(mayus(entrada)) + ' caracteres en MAYUSCULA')
