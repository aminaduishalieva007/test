# list = ["book", "pen", "marker"]
# print(list)


# list = ["book", "pen", "marker"]
# list.append("stapler")
# print(list)


# list = ['book', 'pen', 'marker', 'stapler']
# list.append("1,2,3,")
# print(list)


# list = ['book', 'pen', 'marker', 'stapler', '1,2,3,']
# list.append("glove")
# print(list)


# tuple = ['book', 'pen', 'marker', 'stapler', '1,2,3,', 'glove']
# tuple.append("calculator")
# print(tuple)
 

# list = ['book', 'pen', 'marker', 'stapler', '1,2,3,', 'glove', 'calculator']
# print(list[0:7])


# list = ['book', 'pen', 'marker', 'stapler', '1,2,3,', 'glove', 'calculator']
# list.remove('stapler')
# print(list)
 

# set = {'book', 'pen', 'marker', '1,2,3,', 'glove', 'calculator'}
# print(set)




# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print(a[:5])

# a = [1, 1, 2, 3, 5]
# print(a[0])

# a = [1, 1, 2, 3, 5]
# print(a[-1])

# a = [1, 1, 2, 3, 5]
# print("free"in a)


# str1 = 'Hello'
# str2 = 'World'
# print(str1,str2)


# str = "Hello World"
# print(str.upper())

# s = 'python'
# print(s[::-1])



# a = "Hello, World!"
# print(len(a))



# def сложение(a, x):
#     return a + x
# a = int(input("ввидите первое число: "))
# x = int(input("ввидите второе число: "))
# z = a + x
# print(z)


# a = int(input("ввидите первое число: "))
# x = int(input("ввидите второе число: "))
# def sum(a, x):
#     return a * x

# print(sum(a, x))

    
# def ela():
#     number = random. randint(1,100)
#     tries = 0


#     print("салам ! сен тап 1 до 100 чейин.Аракет кыл !")

#     while True:
#         guess = int(input("сан жазыныз : "))
#         tries += 1
#         if guess < number:
#              print("ушул сандан чон !")
#         elif guess > number:
#               print("ушул сандан кичине !")
#         else:
#             print((f"куттуктайм! Сен таптын санды {number} за {tries} папытка!"))
#             break


# ela()


# import random

# def rd():
#     слова = ["amina", "askat", "sanat", "elaman"]
#     return  random.choice(слова)
    
# def game():
#     lan = red()
#     str = len(lan)
#     попытка = 0
#     rai = 5
#     abc = ['_'] * str 

    # print("Добро пожаловать в игру 'Угадай число!'")
    # print("У вас есть", rai, "попыток. Ваше слово содержит", len, "букв.")
    # while True:
    #     guess  = (input("напиши слова : "))
    #     попытка += 1
    #     if guess < lan:
    #          print("ушул сандан чон !")
    #     elif guess > lan:
    #           print("ушул сандан кичине !")
    #     else:
    #          print((f"куттуктайм! Сен таптын санды {abc} за {попытка} папытка!"))
    #          break






# a = int(input('введите число  '))
# if a %2==0:
#     print('четное')
# else:
#     print('не четное')




# x = lambda a : a + 10
# print(x(23))


# x = lambda a, b, c : a + b + c
# print(x(6, 6, 2))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(6)
# mytripler = myfunc(8)

# print(mydoubler(11))
# print(mytripler(11))


# def myfunc(b):
#   return lambda a : a * b

# mydoubler = myfunc(2)

# print(mydoubler(14))

# x = lambda a, b : a * b
# print(x(23, 9))




# sum = (input('введите:'))

# if sum.isalpha():
#     print('это str')
# elif sum.isdigit():
#     print('это number')
# else:
#     print('это float')


# def even(a):
#     if a%2==0:
#         print(a,'четное')
#     else:
#         print(a,'нечотное')

# for i in range(7, 8):
#             even(i)




# def myfunc(b):
#   return lambda a : a + b

# mydoubler = myfunc(6)

# print(mydoubler(6))

# x = lambda a, b : a * b
# print(x(4, 2))

# x = lambda a, b : a - b
# print(x(9, 9))

# x = lambda a, b : a // b
# print(x(88, 8))


# my_list = [5, 2, 8, 1, 3]
# my_list.sort()
# print(my_list)

# for i in range(1):
#       i = ("python,python,python") 
#       print(i)

# numbers = (1,2,3,4,5,6,7,8,9,10)
# def even(a):
#     if a%2==0:
#         print(a,'четное')
#     else:
#         print(a,'нечотное')

# for i in range(1,11):
#             even(i)


# fruits = {"яблоко", "груша", "апельсин", "банан"}
# fruits.add("orange")
# print(fruits)




# list = [1,2,3,4,5]
# myiter = iter(list)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))



# while True:
#     name = "amina"
#     password = 1223

#     x = str(input("ввидите имя"))
#     nume = int(input("введите пароль"))
#     if x  == name:
#         print("поздравляю вы прошли")
#     if nume == password:
#         print()
#     else: 
#         print('доступ закрыть')



# import calendar
# print("Calendar 2024:")
# print(calendar.calendar(2024))


# a = int(input('оценки: '))
# if 1 < a <= 3:
#     print('не прошел')
# if 3 < a <= 5:
#     print('прошел ')     



# a = int(input('введите число:  '))
# b = int(input('введите число: '))
# if a >= b:
#     print(a,"больше чем", b)
# elif a <= b: 
#     print(b, "больше чем", a)

# for i in range(1):
#       i = ("python,python,python") 
#       print(i)



# def sad(x):
#     print('куб числа',x,'=', x**3)
# sad(25)



# a = int(input("ввидите число: "))

# print("чейин " + str(a-1))
# print("кийин " + str(a+1))


# a = int(input("ввидите число: "))
# print(str(a) + "---" + str(a*2)+ "---" + str(a*3)+ "---" + str(a*4))



# a = int(input("ввидите число: "))
# if a %2==0:
#     print(a//2)
# else:
#     print((a+1)//2)



# a = int(input("ввидите число: "))
# if a>60:
#     b = a%60
#     c = a // 60
#     print(str(a) + "- eto"  + str(c) + "saat" + str(b) + "min"  )


# def func(a):
#     print(a * 0.6214)
# km = int(input("km jaz"))
# func(km)

# class A(Das):
#     def __init__(self,):

# class A(Das):
#     def __init      
# def ab(a, b):
#     c = a+b
#     c.sort()
#     return c 

# print(ab([1, 2, 3],[5, 4, 6, 8]))






   

# class A:
   
#    def __init__(self,lis,lis2):
#       self.lis = lis
#       self.lis2 = lis2


#    def a(self):
#       a = sorted(self.lis+self.lis2)
#       return a
# list = [13,75,10,16]
# list1 = [5,6,343,245]
# b = A(list,list1)
# print(b.a())



# a = int(input('aга сан киргиз'))
# b = int(input('bга сан киргиз'))
# if (a>b):
#             print('чон сан = : a' )
# elif (a<b):
#         print('барабар')




# a = int(input("Введите start1 от 1 до 8: "))
# b= int(input("Введите star2 от 1 до 8: "))
# a1 = int(input("Введите конец1 от 1 до 8: "))
# b1 = int(input("Введите конец2 от 1 до 8: "))
# if a == b or a1 == b1:
#     print(True)
# else:
#     print(False)



# a = int(input('san jaz'))

# if a%3!=0:
#     print('bolynboit')
# else:
#     print('bolynot')


# a = int(input('san jaz'))
# b = int(input('san jaz'))
# c = int(input('san jaz'))

# if a < c and c > b:
#     print(c)
# elif a < b and c < b:
#     print(b)
# else:
#     print(a)

# a = []
# n = int(input())
# for i in range(n):
#     b = int(input())
#     a.append(b)

# t = 1000

# for i in a:
#     if i < t:
#       t = i
# print(t)

# a = int(input())

# try:
#     print(a / 0)
# except:
#     print('sandy nolgo bolso bolboit')
# else:
#     print('askatgyl')



# def methot_plus(*args):
#     try:
#         s = 0
#         for i in args:
#             s = s + i
#     except TypeError:
#         print('str menen int koshulbait!')
# methot_plus(2345,'geg')

