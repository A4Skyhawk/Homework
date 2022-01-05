file1 = open('16-12-2021_D3.txt', 'r')
A = ['']
i = 0 
p = 0

while True:
    line = file1.readline()
    if not line:
        break
    (A).append(line.strip())
    i += 1

for i in range(len(A)):
    A[i] = A[i].replace(',', ' ')
    A[i] = A[i].replace('!', ' ')
    A[i] = A[i].replace('–', ' ')
    A[i] = A[i].replace('.', ' ')
    A[i] = A[i].replace(':', ' ')
    A[i] = A[i].replace(';', ' ')
print(A)

B = ['']
k = 0

for i in range(len(A)):
    p = 0
    for j in range(1,len(A[i])):
        if (A[i][j] == (' ')) :
            B.append(A[i][p:j])
            p = j
            k +=1
print(B)

print('def')
for i in range(len(B)):
    B[i] = B[i].replace(' ', '')
print(B)

print('def')
for i in range(len(B)):
    B[i] = B[i].lower()
print(B)

C = ['']
print('def')
i = 0
for i in range(len(B)):
    if B[i] != (''):
        C.append(B[i])
        i += 1
C.remove('')
print(C)

D = {}
BigD = {}
for i in range(len(C)):
    s = C.count(C[i])
    D = {C[i]: s}
    BigD.update(D)

print(BigD)

print(max(BigD.values()))

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

A = ['']
i = 0 
p = 0

while True:

    line = file1.readline()

    if not line:
        break

    (A).append(line.strip())
    i += 1


for i in range(len(A)):
    A[i] = A[i].replace(',', ' ')
    A[i] = A[i].replace('!', ' ')
    A[i] = A[i].replace('–', ' ')
    A[i] = A[i].replace('.', ' ')
    A[i] = A[i].replace(':', ' ')
    A[i] = A[i].replace(';', ' ')
print(A)

B = ['']
k = 0

for i in range(len(A)):
    p = 0
    for j in range(1,len(A[i])):
        if (A[i][j] == (' ')) :
            B.append(A[i][p:j])
            p = j
            k +=1
print(B)

print('def')
for i in range(len(B)):
    B[i] = B[i].replace(' ', '')
print(B)

print('def')
for i in range(len(B)):
    B[i] = B[i].lower()
print(B)

C = ['']
print('def')
i = 0
for i in range(len(B)):
    if B[i] != (''):
        C.append(B[i])
        i += 1
C.remove('')
print(C)

D = {}
BigD = {}
for i in range(len(C)):
    s = C.count(C[i])
    D = {C[i]: s}
    BigD.update(D)

print(BigD)

print(max(BigD.values()))

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

print('Искомое значение:',get_key(BigD,(max(BigD.values()))))
