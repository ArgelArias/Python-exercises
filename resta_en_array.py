import random

def subst_in_array(array,target):
    sub = 1
    x = 0
    y = 0
    z = 0
    while(sub != target):
        sub = 0
        x = random.randint(0, len(array) -1)
        y = random.randint(0, len(array) -1)
        z = random.randint(0, len(array) -1)
        sub = array[x] - array[y] - array[z]
    return array[x], array[y], array[z]

array = [10,20,10,40,50,60,70]
print(subst_in_array(array, 50))

array = [-25, -10, -7, -3, 2, 4, 8, 10]
print(subst_in_array(array, 0))
