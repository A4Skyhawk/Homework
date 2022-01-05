print ('Введите последовательность, закончив её нулём')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

print('Объектов, больших соседей:')

for i in range (1,(len(A)-2)):
    if (A[i]>A[i-1]) and (A[i]>A[i+1]):
        S += 1
        

print(S) #лютейший костыль
