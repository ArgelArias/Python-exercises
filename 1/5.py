def sum(*nums):
    final = 0
    for num in nums:
        final += num
    return final

def multi(*nums):
    if(len(nums) > 0):
        final = 1
    else:
        final = 0
    for num in nums:
        final *= num
    return final

print(sum(1,2,3,4))
print(multi(1,2,3,4))
print(multi())
