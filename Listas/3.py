def ordenada(lista):
    sorted = list(set(lista)) #set() creates a set object, in an ordered way, list() casted it list object back
    if(sorted == lista):
        return True
    else:
        return False

print(ordenada([1,2,3]))
print(ordenada(['b','a']))
