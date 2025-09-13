def max(*nums):
    max = 0
    for num in nums:
        if(num > max):
            max = num
    return max

print(max(7,10,14))
print(max(10,10,14))
print(max(7,7,7))
print(max(7,7,7,13,15))

input()
exit()
