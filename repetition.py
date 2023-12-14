from math import sqrt

# str Строка
# int 23
# float 23.23
# set {23, 'u4u'}
# frosenset a = frosenset(23, 'u4u') a.add(1) Error
# tuple (21, [])
# dict() {Неиз тип данных: []}
# list [1, 'ERW']
# boolean True False
#
# a = []
# n = int(input())
# for i in range(n):
#     b = int(input())
#     a.append(b)
#
# t = 1
# for i in a:
#     if i > t:
#         t = i
# 5
# 1
# 3
# 4
# 5
# 6


def method_args(*args):
    print(type(args))


# method_args(1, 2, 'jkasdf', [1])


def method_kwargs(**kwargs):
    print(type(kwargs), kwargs)


# method_kwargs(askat=16, sanat=16, amina=17)


# a = int(input())
# # b = int(input())
#
# try:
#     print(a / 0)
# except:
#     print('sandy nolgo bolso solboit')
# else:
#     print('lksdjf')


def method_plus(*args):
    try:
        s = 0
        t = 0
        b = 0
        for i in args:
            s += i
            t = 10 / i
            b = sqrt(i)
    except TypeError:
        print('TypeError')
    except ValueError:
        print('ValueError')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    else:
        print(f's={s}\nt={t}\nb={b}')
    finally:
        print('Programma ayalktady')


method_plus(1, 2)
