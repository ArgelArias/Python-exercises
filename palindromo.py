def IsCasiPalindromo(palabra):
    count = 0
    rev_index = -1
    for i in range(0, int(len(palabra)/2)):
        print(i, rev_index, count)
        if(palabra[i] != palabra[rev_index]):
            count += 1
        rev_index -= 1
    if(count <= 1):
        return True
    else:
        return False

print(IsCasiPalindromo('abccba'))
print(IsCasiPalindromo('abccbx'))
print(IsCasiPalindromo('abccfg'))


def Palindromo(palabra):
    rev_index = -1
    for i in range(0, int(len(palabra)/2)):
        if(palabra[i] != palabra[rev_index]):
            return False
        rev_index -= 1
    return True

print(Palindromo('abccba'))
print(Palindromo('abccbx'))
print(Palindromo('abccfg'))
print(Palindromo('anitalabalatina'))
