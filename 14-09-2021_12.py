print ('Введите значения, закончив их нулём')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

imax = 0
maxi = 0

for i in range(len(A)):
    if A[i]>maxi:
        maxi = A[i]
        imax = i

print (maxi,' ',imax)
