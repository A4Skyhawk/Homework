print ('Введите список, закончив его числом 0')
A = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    A.insert(i,(buff))
    buff = int(input())


print('Введите число k')
k = int(input())

dl = len(A)

while k in A:
    A.remove(k)

A.pop(0)
A.pop(len(A)-1)

print (A)
