class Time:
     def __init__(self,h,m,s):
         self.h = h
         self.m = m
         self.s = s
         self.time_check()

     def __str__(self):
         return f"Время: {self.h} часов, {self.m} минут, {self.s} секунд"

     def diff(self,time2):
         self.h -= time2.h
         self.m -= time2.m
         self.s -= time2.s
         self.time_check()
         return f"Разница времени: {self.h} часов, {self.m} минут, {self.s} секунд"

     def plus(self,time2):
         self.h += time2.h
         self.m += time2.m
         self.s += time2.s
         self.time_check()
         return f"Результирующее время: {self.h} часов, {self.m} минут, {self.s} секунд"

     def time_check(self):
         if self.s >= 60:
             self.m = self.s//60
             self.s = self.s % 60
         if self.m >= 60:
             self.h = self.m//60
             self.m = self.m % 60
         if self.h >=24:
             self.h = self.h % 24
         
Moscow = Time(12,0,0)
print(Moscow)
London = Time(8,0,0)
print(Moscow.diff(London))
print(Moscow.plus(London))
print(Moscow.plus(London))
print(Moscow)
print(Moscow.plus(London))
