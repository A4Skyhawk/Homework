print('Введите координаты')

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())



def distance(x1,x2,y1,y2):
    X = abs(x1-x2)
    Y = abs(y1-y2)
    S = (X*X+Y*Y)**0.5
    return(S)

print(distance(x1,x2,y1,y2))
