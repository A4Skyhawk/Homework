print('Введите числа через пробел, закончив числом 000')
S = str(input())

a = set(S)
b = [0]*len(a)
k = 1
p = 1

for i in range(1,len(S)):
    if S[i] == (' '):
        b[k] = S[p-1:i+1]
        p = i+1
        k += 1
        
print(b)
print(a)
for i in range(1,len(b)):
    if int(b[i]) in a:
        print('YES')
    else:
        print('NO')


