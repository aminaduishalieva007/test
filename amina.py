# from turtle import *

# t = Turtle()
# bgcolor("black")
# t.pencolor("yellow")
# t.speed(0)
# for i in range(320):
#     t.circle(190-i, 90)
#     t.left(90)
#     t.circle(190-i, 90)
#     t.left(18)
#     if i > 190:
#         t.persize(3)

#         mainloop()



# first_name = input('Имя')
# middle_name = input('Отчество')
# last_name= input('Фамилия')
# age = int(input('Возвраст'))
# print(f'Добрый день, {last_name} {first_name} {middle_name}\nВам {age} лет')


# row = int(input("Enter number of rows: "))

# print("Generated Hourglass Pattern is: ")
# #Upper-half
# for i in range(row, 0, -1):
#     for j in range(row-i):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()

# #Lower-half
# for i in range(2, row+1):
#     for j in range(row-i):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()