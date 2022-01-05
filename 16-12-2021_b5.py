
S = str(input())
a = set()
i = 0
p = 0

for i in range(1,len(S)+1):
    if (i == len(S)) or (S[i] == (' ')):
        a.add(S[p:i])
        p = i+1

print(len(a))
