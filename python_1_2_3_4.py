# создание класса, описывающего студента
# класс - это описание студента (по крайней мере тут)
class Student:
    # функция для создания объекта
    def __init__(self, name, age, surname, sex, stud):
        # заполняем поля-переменные объекта
        self.name = name
        self.age = age
        self.surname = surname
        self.sex = sex
        self.stud = stud
        
    def look_naskvozy(self):
        print(self.name,',',self.age,',',self.surname,',',self.sex,',',self.stud)

#объекты по шаблону
#имя возраст фамилия
#пол+цифры

s1 = Student("Степан",17,"Бандера","М",346468)
s2 = Student("Остап", 18,"Бендер","М",124362)
s3 = Student("Уинстон",71,"Черчилль","М",134794)
s4 = Student("Михаил",16,"Погосян","М",157241)
s5 = Student("Львица",19,"Семитысячная","Ж",177013)
s6 = Student("Насвай",18,"Жирафов","М",177013)
s7 = Student("Бинина",183576,"Мибиткибина","Ж",177013)
#расстрельный список из студентов
students = [s1, s2, s3, s4, s5, s6, s7]

for i in range(0,len(students)):
    print(students[i].look_naskvozy())

#2

students_age = [s1.age, s2.age, s3.age, s4.age, s5.age]

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
            print(students[j].naidi_raboty())
            students_age[j] = ''


#3
print('ТРЕТИЙ qo')
students_age = [s1.age, s2.age, s3.age, s4.age, s5.age]
def bin_search(target, nums):
    # определяем границы поиска
    l = 0
    r = len(nums) - 1
    while l <= r:
        # вычисляем индекс числа посередине
        m = (l + r) // 2
        guess = nums[m]
        # сравниваем это число с искомым
        if guess == target:
            return m
        # если проверяемое число не совпадает с искомым,
        # то определяем половину, в которой находится искомое число
        if target < guess:
            # нужно рассмотреть левую половину, поэтому сдвигаем правый указатель за середину
            r = m - 1
        else:
            # нужно рассмотреть правую половину, поэтому сдвигаем левый указатель за середину
            l = m + 1
    # возвращаем -1 если в цикле ни один элемент не прошел условие
    return ('Dear god')
    


#есть упорядоченный массив из чисел
students_age = [s1.age, s2.age, s3.age, s4.age, s5.age]
sigma = bubble_sort(students_age)
target = 31

#используем функцию для поиска индекса числа в массиве
#ind = linar_search(target, nums)
ind = bin_search(target, sigma)

#выводим число и его индекс
if ind == 'no':
    print("Число %d не было найдено!" % target)

for j in range (len(students)):
    if (target == students_age[j]):
        print(students[j].look_naskvozy())
        break
