print ('Введите значения, закончив их нулём')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

maxi = 0

for i in range(len(A)):
    if A[i] == A[i-1]:
        S += 1
    else:
        if S> maxi:
            maxi = S
        S = 0

print (maxi+1)
        
