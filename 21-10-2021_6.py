print ('Введите значения списка, закончив их нулём')
A = [1]
S = 0 
i = -1
j = 0
buff = 1
while buff != 0:
    i +=1
    A.insert(i,(buff))
    buff = int(input())

A.pop(0)
A.pop(len(A)-1)

print(A)

B = A

for i in range (1,(len(A)//2)*2):
    buff = A[i-1]
    B[i] = buff
    print(A[i-1])
    buff = A[i]
    B[i-1] = buff

print(B)
