Fail = open('name.txt',encoding='utf-8')
print(Fail.readlines()) 
Fail.close()
print(Fail.closed) 




list = [1, 2, 3, 4, 5, 6]
a = iter(list)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))