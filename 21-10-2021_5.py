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

    
B = A 

for i in range(len(A)-1):
    for j in range(len(A)-1):
        if (A[i] == A[j]) and (i!=j):
            B[i] = 0
            B[j] = 0

while 0 in B:
    B.remove(0)


print (B)
            
        
        

