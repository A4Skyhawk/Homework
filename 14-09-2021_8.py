print ('Введите последовательность, закончив её нулём')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

print('Объектов, больших предыдущёго:')

for i in range (len(A)):
    if A[i]>A[i-1]:
        S += 1
        

print(S-2) #лютейший костыль
