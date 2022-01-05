print ('введите число')
n = int(input())
i = n//2
nnd = 0
for i in range(n//2,2,-1):
    if (n%i == 0):
        nnd = i
        
print (nnd)
