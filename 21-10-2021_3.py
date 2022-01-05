print ('Введите значения списка, закончив их нулём')
A = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    A.insert(i,(buff))
    buff = int(input())

sorted(A)

print(A[2])

