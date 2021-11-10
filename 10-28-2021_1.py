print ('Введите значения списка, закончив их нулём')
B = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    B.insert(i,(buff))
    buff = int(input())
B.remove(1)
B.pop(len(B)-1)

def srar(B):
    S = 0
    for i in range(len(B)):
        S += B[i]
    return S/len(B)

print(B)
print(srar(B))
