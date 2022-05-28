# создание класса, описывающего студента
# класс - это описание студента (по крайней мере тут)
class studentus:
    # функция для создания объекта
    def __init__(self, name, surname, age, sex, stud):
        # заполняем поля-переменные объекта
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.stud = stud
        
def look_naskvozy(self):
    print(self.name,',',self.surname,',',self.sex,',',self.age,',',self.stud)

#объекты по шаблону
#имя фамилия
#пол+цифры

s1 = studentus("Василий","Чапаев",43,"М",346468)
s2 = studentus("Остап","Бендер",18,"М",124362)
s3 = studentus("Уинстон","Черчилль",71,"М",134794)
s4 = studentus("Жанна","Д'Арк",26,"Ж",157241)
s5 = studentus("Львица","Семитысячная",89,"Ж",177013)
s6 = studentus("Насвай","Жирафов",18,"М",177013)
s7 = studentus("Бинина","Мибиткибина",183576,"Ж",177013)

#расстрельный список из студентов

students = [s1, s2, s3, s4, s5, s6, s7]

for i in range(0,len(students)):
    print(students[i].look_naskvozy())

#2

students_age = [s1.age, s2.age, s3.age, s4.age, s5.age, s6.age, s7.age]

def bubble_sort(c):
    # создаем копию массива
    a = c[:]
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

d = bubble_sort(students_age)

for i in range(len(d)):
    for j in range (len(students)):
        if (d[i] == students_age[j]):
            print(students[j].look_naskvozy())
            students_age[j] = ''


#3
print('3qo')
students_age = [s1.age, s2.age, s3.age, s4.age, s5.age]
def bin_search(target, nums):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        guess = nums[m]
        if guess == target:
            return m
        if target < guess:
            r = m - 1
        else:
            l = m + 1
        return ('Dear god')
    
