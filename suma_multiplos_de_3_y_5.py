def suma_multiplos_de_3_y_5(num):
    total = 0
    for i in range(1,num):
        if(i % 3 == 0):
            #print(i)
            total += i
        if(i % 5 == 0):
            #print(i)
            total += i
    return total

print(suma_multiplos_de_3_y_5(1000))
