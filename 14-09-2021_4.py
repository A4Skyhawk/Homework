print ('Введите номер числа')
n = int(input())
fib = [0]*(n+1)
fib[1] = 1 
for i in range(1,n+1):
    fib[i] = fib[i-1] + fib[i-2]
    fib[1] = 1
    print (fib[i])

print (fib[n])
