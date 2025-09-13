def dec2rom(num):
    vals={1:'I', 4:'IV', 5:'V', 9:'IX',
          10:'X', 40:'XL', 50:'L', 90:'XC',
          100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
    final = ''
    for val, letter in sorted(vals.items(), reverse=True):
        while(num >= val):
            final += letter
            num -= val
    return final

def rom2dec(num):
    vals={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    final = 0
    for index in range(len(num)):
        if(index > 0 and vals[num[index]] > vals[num[index -1]]):
            final += vals[num[index]] - (2 * vals[num[index -1]])
        else:
            final += vals[num[index]]
    return final


print(dec2rom(5000))
print(dec2rom(1990))

print(rom2dec('MMXII'))
