print ('Введите значения, закончив их нулём')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

sorted(A)

maxi = A[1]

for i in range (1,len(A)):
    if A[i] == A[1]:
        S += 1

print (S)
