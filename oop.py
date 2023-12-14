# class Amina:
#     def __init__(self,name,surname,age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#     def askat(self):
#         print(self.name)
#     def sanat(self):
#         print(self.surname)
#     def noodir(self):
#         print(self.age)
# a = Amina('Amina',"Duishalieva",16)
# a.askat()
# a.sanat()
# a.noodir()


# class Calkulator:
#     def __init__(self,number,operation,san2):
#         self.number = number
#         self.operation = operation
#         self.san2 = san2
#     def plus(self):
#         if self.operation == '+':
#             print(self.number + self.san2)
#     def minus(self):
#         if self.operation == '-':
#             print(self.number - self.san2)
#     def umnojn(self):
#         if self.operation == '*':
#             print(self.number * self.san2)
#     def delenie(self):
#         if self.operation == '/':
#             print(self.number / self.san2)

# cal = Calkulator(7, '+', 3)
# cal.plus()
# cal = Calkulator(7, '-', 3)
# cal.minus()
# cal = Calkulator(7, '*', 3)
# cal.umnojn()
# cal = Calkulator(21, '/', 3)
# cal.delenie()


# class Student:

#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname

#     def get_name(self):
#         return self.__name
    
#     def get_name(self, name):
#         return self.__name
    
#     def get_surname(self):
#         return self.__surname
    
#     def set_surname(self, surname):
#         self.__surname = surname

# student_1 = Student("Sanat" , "Ishenbekov")
# print(student_1.get_surname())
# student_1.set.surname("Mahamadjanov")
# print(student_1.get_surname())


# class Telefon:
#     def __init__(self, name, gb,):
#         self.name = name
#         self.gb =gb
        
#     def a(self):
#         print(self.name)
#     def b(self):
#         print(self.gb)

# p = Telefon('Samsung', '64')
# p.a()
# p.b()


# class Tele(Telefon):
#     def __init__(self, name, gb, color):
#         self.name = name
#         self.gb =gb
#         self.color = color
#     def a(self):
#         print(self.name)
#     def b(self):
#         print(self.gb)
#     def c(self):
#         print(self.color)

# p = Telefon('iphone', '215', 'blac')
# p.a()
# p.b()
# p.c()

# class Telefon:
#     def __init__(self, name, gb, color):
#         self.name = name
#         self.gb =gb
#         self.color = color
#     def a(self):
#         print(self.name)
#     def b(self):
#         print(self.gb)
#     def c(self):
#         print(self.color)

# p = Telefon('Samsung', '64', 'black')
# p.a()
# p.b()
# p.c()


# class Phone:
#   def __init__(self,model,color):
#     self.model = model
#     self.color = color

#   def print(self):
#     print(self.model, self.color)

# p = Phone("iphone", "black")
# p.print()

# class Pho(Phone):
#   def __init__(self, model, color, gb):
#     super().__init__(model, color)
#     self.gb = gb

#   def func(self):
#     print(self.gb, self.color, self.model)

# x = Pho("samsung", "black", "64")
# x.func()




# class Student:
#     def __init__(self, name, lastname):
#         self.name = name 
#         self.lastname = lastname 

#     def func(self):
#         print("hellow", self.name, self.lastname)

# l = Student("Askat", "Burhanov")
# l.func()


# class Boy(Student):
#     def __init__(self, name, lastname, age):
#         super().__init__(name, lastname)
#         self.age = age

#     def func_def(self):
#         print(self.age, self.name, self.lastname)

# b = Boy("Esen", "Asanov", "12")
# b.func_def()

# class Student:
#     def __init__(self, age):
#         self.age = age 

#     def func(self):
#             for i in range(self.age):
#                 print(i)

# s = Student(5)
# s.func()

#  def find_all(soz, tamga):
#     a = 0
#     for i in soz:
#         if i==tamga:
#             a = a+1
#     return a 


# a = str(input("soz jaz: "))
# b = str(input("tanga jaz: "))
# print(find_all(a, b))

# class A:
#     def __init__(self, soz, tamga):
#         self.soz = soz 
#         self.tamga = tamga 

#     def func(self):
#         for i in range(self.age):
#                 print(i)
#         print(self.soz, self.tamga)
    
# s = input('soz jaz: ')
# b = input("tamga jaz: ")
# s = A(5)
# s.func()

# class Das:
#    def __init__(self,soz):
#       self.soz = soz




   

# class A(Das):
#    def __init__(self,soz, tamga):
#       super().__init__(soz)
#       self.tamga = tamga
   

#    def tamga1(self):
#       a = 0
#       for i in self.soz:
#          if i == self.tamga:
#             a = a +1
#       return a

# x = input('soz: ')
# y = input('tamga: ')

# a = A(x,y)
# print(a.tamga1())

# class Transport:
#     def __init__(self,maxskorost,probel,name):
#         self.maxskorost = maxskorost
#         self.probel = probel

# matz = Transport(240, 60)
# print(matz.maxskorost)



# class Transport:
#     def __init__(self, name):
#         self.name = name 

#     def cap(self,capacity):
#         return f"{self.name} transportunun orundugunun sany: {capacity}" 
    
    

# bus = Transport("Bus")
# print(bus.cap(20))




# class Magazin:
#     name = str
#     size = str
#     price:float

#     def __init__(self, name, size, price):
#         self.name = name
#         self.size = size
#         self.price = price 
        
# class Obuv:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color =color
 
#     def func(self):
#          print(f'{self.brand}, {self.color}')

# a = Obuv('adidas', 'black')
# a.func()



# class Calculate:
#     def boluu(self, a, b):
#         return a//b
    
#     def koboitu(self, a, b):
#         return a*b
    
#     def koshuu(self, a, b):
#         return a+b
    
#     def kemituu(self, a, b):
#         return a-b
    
# class B(Calculate):
#     def __init__(self, a, b, t):
#         self.a = a 
#         self.b = b
#         self.t = t
        
#     def ask(self):
#         if self.t=='+':
#             return self.koshuu(self.a,self.b)
#         elif self.t=='-':
#             return self.kemituu(self.a,self.b)
#         elif self.t=='*':
#             return self.koboitu(self.a,self.b)
#         else:
#             return self.boluu(self.a,self.b)
        
# c = B(6,9,'*')
# print(c.ask())