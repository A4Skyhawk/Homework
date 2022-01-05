#Random bullshit, go!
file1 = open('16-12-2021_D6.txt', 'r')
A = []
i = 0 
p = 0

while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # записываем строку
    (A).append(line.strip())
    i += 1

B = []
F = []
k = 0

# разбивка на слова
for i in range(len(A)):
    p = 0
    for j in range(1,len(A[i])):
        if (A[i][j] == (' ')) :
            k += 1
            if k == 2:
                B.append(A[i][0:j])
                F.append(int(A[i][j+1:len(A[i])])) #числа
                k = 0
                break

print(F)

    

#займёмся подсчётами
D = {}
BigD = {}
bruh = ''
for i in range(len(B)):
    for j in range(len(B)):
        if (B[i] == B[j]) and (i != j):   
            D = {B[i]: F[i]+F[j]}
            B[j] = ''
            F[j] = 0
            bruh = B[i]
            BigD.update(D)
            k += 1
        else:
            if bruh in B:
                B[B.index(bruh)] = ''
            D = {B[i]: F[i]}
            BigD.update(D)

print(str(BigD))
#Работает, пусть и оставляет мусор

