import random

def sum_in_array(array,target):
    sum = 0
    x = 0
    y = 0
    while(sum != target):
        sum = 0
        x = random.randint(0, len(array) -1)
        y = random.randint(0, len(array) -1)
        sum = array[x] + array[y]
    return x, y

array = [10,20,10,40,50,60,70]
print(sum_in_array(array, 50))
