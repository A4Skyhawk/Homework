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

print(A)

for i in range(0,len(A)-1):
    if A[i] == A[i+1]:
        S += 1

print(S)
