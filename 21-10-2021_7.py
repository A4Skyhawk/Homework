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

print('Введите k')
k = int(input())
k -= 1
v = k
for i in range(k+1,len(A)):
    A.insert(v,A[i])
    A.pop(A[i+1])
    v +=1

A.pop()
print(A)
