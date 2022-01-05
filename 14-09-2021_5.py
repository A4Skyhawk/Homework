print ('Введите длину списка')
n = int(input())
A = ['']*n

for i in range (n):
    A[i]=str(input())

for i in range (n):
    if i%2 == 0:
        print(A[i])
