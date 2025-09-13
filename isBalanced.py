def isBalanced(str):
    simbols = {'(': ')'}
    stack = []
    for i in range(len(str)):
        if str[i] in simbols.keys():
            stack.append(str[i])
        elif str[i] in simbols.values() and len(stack) > 0:
            if str[i] == simbols[stack[len(stack) -1]]:
                stack.pop()
            else:
                return False
    if(len(stack) > 0):
        return False
    return True

print(isBalanced('(aaa)(b)'))
print(isBalanced('(aa)(bb)'))
print(isBalanced('(())'))
print(isBalanced('('))
print(isBalanced('(()'))
