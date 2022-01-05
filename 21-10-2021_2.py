print ('Введите число А')

A = int(input())
fib = [0]*10000
fib[1] = 1 
for i in range(2,A+5):
        fib[i] = fib[i-2] + fib[i-1]
        if A == fib[i]:
            print(' ',i)
            break
        elif A<i:
            print (-1)
