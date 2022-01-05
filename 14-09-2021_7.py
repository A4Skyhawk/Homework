print ('Введите длину массива')
n = int(input())
A = [0]*(n+1)
print ('Введите список чисел со знаками + и -')

for i in range (n):
    A[i] = int(input())

for i in range (n):
    if (A[i]>=0 and A[i+1]>=0) or (A[i]<0 and A[i+1]<0):
        print(A[i],A[i+1])
        break
    
