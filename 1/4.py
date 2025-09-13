import re

def vocal(car):
    #if(car == 'a' or car == 'e' or car == 'i'or car == 'o'or car == 'u'):
    if(re.search("a|e|i|o|u", car)):
        return True
    else:
        return False

print(vocal('a'))
print(vocal('b'))
print(vocal('c'))
print(vocal('e'))
print(vocal('i'))
print(vocal('v'))
