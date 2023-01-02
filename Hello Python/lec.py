
# a = 123
# print(type(a))

# s = "Hello world"

# print(type(s))

# s = "Hello \n world" # переход на другую строку

# list = [1,2,56,56]
# print(list)

# print('Введите а');
# a = int(input())
# print('Введите b');
# b = int(input())
# c = a + b
# print(a, ' + ', b, ' = ', c)
# print('{} + {} = {}'.format(a, b, c))

# a = 12
# b = 5
# c = 12 // 5 
# d = a ** 5 # возведение в степень
# print(c)
# print(d)

# a = 1.3
# b = 3
# c = round(a * b, 3) # функция округления
# print(c)

# f = [1,2,3,4,5]
# print(2 in f)

# a = int(input("a= "))
# b = int(input("b= "))
# if a > b:
#     print(a)
# else:
#     print(b)


original = 23
inverted = 0
while original != 0:
 inverted = inverted * 10 + (original % 10)
 original //= 10
else:
 print('Пожалуй')
 print('хватит )')





# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# N = int(input("Введите  число N: "))
# for i in range(-N, N+1):
#     print(f'{i},  ',end='')

# number = int(input("Введите число: "))
# my_str = ''
# for i in range(-number, number+1):
#     my_str += str(i) + ', '
# print(my_str[:-2])

# number = int(input("Введите число: "))
# my_list = []
# for i in range(-number, number+1):
#     my_list.append(i)  
# print(*my_list, sep=", ")


# Кирилл (Стоун): 2. Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# -- Вариант 1
# number = float(input("Введите число: "))
# ost = int(number * 10) % 10
# if number == int(number):
#     print("нет")
# else:
#     print(ost)

# -- Вариант 2
# num = input("Введите число: ")
# num = num.split(".")
# if len(num) < 2:
#     print("целое")
# else:
#     print(num [1] [0])



