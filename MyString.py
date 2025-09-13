class MyString:
    string = ''

    def get_string(self, string):
        self.string = string

    def inverted(self):
        newString = ''
        lenght = len(self.string)
        while(lenght > 0):
            newString += self.string[lenght -1]
            lenght -= 1
        return newString

my_string = MyString()
my_string.get_string(input('Inserte una cadenda : '))
print(my_string.inverted())
