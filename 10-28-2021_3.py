print('Введите число лет')
years = int(input())

print('Введите количество денЯк')
a = int(input())

def bank(years,a):
    i = 0
    for i in range (years):
        a += 0.1*a
    return (a)

print(bank(years,a))
