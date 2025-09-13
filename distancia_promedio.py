import math

def distancia(x1,y1,x2,y2):
    return math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))

def distancia_promedio(x1,y1,x2,y2,x3,y3):
    distancia1 = distancia(x1,y1,x2,y2)
    distancia2 = distancia(x1,y1,x3,y3)
    distancia3 = distancia(x2,y2,x3,y3)
    return (distancia1 + distancia2 + distancia3) / 3

x1 = 2
y1 = 3
x2 = 5
y2 = 24
x3 = 7
y3 = 10

print(distancia_promedio(x1,y1,x2,y2,x3,y3))
