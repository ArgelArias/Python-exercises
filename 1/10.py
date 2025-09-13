import histograma

def procedimiento(nums):
    for num in nums:
        final = ''
        for i in range(num):
            final = histograma.histograma(i)
        print(final)

procedimiento([4,9,7])
