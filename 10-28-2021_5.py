print ('Введите число и степень, в которую его нужно возвести')

a = int(input())
n = int(input())

def power(a,n):
    m = a
    for i in range(n):
            a *= m
    if n>0:
        return (a)
    elif n<0:
        return (1/a)
    elif n == 1:
        return (1)

print(power(a,n))
