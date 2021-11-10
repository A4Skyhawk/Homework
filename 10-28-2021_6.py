print ('Введите число')
a = int(input())

def is_prime(a):
    for i in range (2,1000):
        if a%i != 0:
            return True
            break
        else:
            return False
           

print (is_prime(a))
