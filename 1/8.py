def superposicion(a, b):
    for item in a:
        if(item in b):
            return True
    else:
        return False

array1 = [1,2,3,4]
array2 = [5,2,7,8]

print(superposicion(array1,array2))
