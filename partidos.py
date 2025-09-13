count = 0
val = 567

for i in range(val):
    count += i

print(count)

count = 0
for i in range(1000,9999):
    if(i % 5 == 0  and i % 7 == 0):
        count += 1

print(count)


for i in range(1536):
    print(i)
