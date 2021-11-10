def bin(a):
    i = 0
    binar = ['1']
    while a>1:
        binar.append(str(a%2))
        a = a//2
        i += 1
    return("".join(binar))

def dec(b):
    i = 0
    decim = 0
    while len(b)!=0:
        decim += (int(b)%10)*(2**i)
        b = b[:(len(b)-1)]
        i += 1
    return(decim)


print('Введите число в десятичной системе')

a = int(input())
print('Оно в двоичной:',bin(a))

print('Введите число в двоичной')

b = str(input())
print('Оно в десятичной:',dec(b))
