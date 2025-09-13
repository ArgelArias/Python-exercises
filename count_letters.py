def count_letters(word):
    dictionary = {}
    for letter in word:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary

print(count_letters('aaaabba'))
print(count_letters('zxyyp'))
print(count_letters(''))
