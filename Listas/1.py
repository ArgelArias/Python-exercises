def acum(nums):
    acumulate = 0
    final = []
    for num in nums:
        acumulate += num
        final.append(acumulate)
    return final

print(acum([1,2,3,4,5,6,7,8,9,10]))
