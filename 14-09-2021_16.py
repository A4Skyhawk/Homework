print ('Введите значения первого списка, закончив их нулём')
A = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    A.insert(i,(buff))
    buff = int(input())
    



print ('Введите значения второго списка, закончив их нулём')
B = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    B.insert(i,(buff))
    buff = int(input())

A.remove(1)
B.remove(1)

Sum = 0
C = [1]

if len(A) == len(B):
    for i in range (len(A)):
        Sum += A[i]*B[i]

print(Sum-1)
