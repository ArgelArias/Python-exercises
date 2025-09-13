def check(string):
    print(string)
    simbols = {'(': ')',
               '[': ']',
               '{': '}'}
    stack = []
    for i in range(len(string)):
        if string[i] in simbols.keys():
            stack.append(string[i])
        elif string[i] in simbols.values() and len(stack) > 0:
            if string[i] == simbols[stack[len(stack) -1]]:
                stack.pop()
            else:
                return 'Invalid String!!!'
        else:
            return 'Invalid String!!!'
    if(len(stack) > 0):
        return 'Invalid String!!!'
    return 'Valid String!!!'


#{[()]}
print(check('{[()]}'))
print(check('{[({}[][()])]}'))
print(check(')]}'))
print(check('[)'))
print(check('({[)]'))
print(check('{{{'))
