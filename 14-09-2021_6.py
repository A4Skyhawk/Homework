print ('Введите длину списка')
n = int(input())
A = ['']*n

for i in range (n):
    A[i]=int(input())

for i in range (n):
    if A[i]%2 == 0:
        print(A[i])
