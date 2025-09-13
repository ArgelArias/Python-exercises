import random

def duplicado(nums):
    for num in nums:
        if(nums.count(num) > 1):
            return True

def ale23():
    ale = []
    for i in range(23):
        ale.append(random.randrange(1,100,1))
    print(ale)
    if(duplicado(ale)):
        return 'La lista de 23 numeros random, tiene duplicados'
    else:
        return 'La lista de 23 numeros random, NO tiene duplicados'

print(ale23())
