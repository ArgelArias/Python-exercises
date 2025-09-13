def found_rep(arr,ent):
    found = 0
    for item in arr:
        if item == ent:
            found += 1
    return found

arr = [2,3,4,3,2,1]
ent = 3

print(found_rep(arr,ent))

