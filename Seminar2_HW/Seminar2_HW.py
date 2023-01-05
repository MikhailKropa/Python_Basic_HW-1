
# ЗАДАЧА 1.
# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# number = float(input('Введите вещественное число: '))

# if number < 0:
#     number = number * (-1)

# k = 0
# for i in str(number):
#     if i != '.':
#         k += int(i)

# print(f'{number} ->', end=' ')
# print(k)


# ЗАДАЧА 2.
# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n = int(input('Введите число n: '))
# dic = {}
# for i in range(1, n + 1):
#     dic[i] = (1+1/i)**i

# t = list(dic.values())

# res = round(sum(dic.values()),2)

# print(f'Для n= {n} -> {t}')
# print(f'Сумма {res}')


# ЗАДАЧА 3.
# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int


import random

My_list = []

for i in range(10):
    My_list.append(random.randint(0,100))


print ("список до перемешивания: " + str(My_list))


for i in range(len(My_list)-1, 0, -1):
    j = random.randint(0, i + 1)
    My_list[i], My_list[j] = My_list[j], My_list[i]
print ("список после перемешивания: " +  str(My_list))













# print(My_list)

# import random
# Mylist = [0,1,2,3,4,5,6,7,8,9]
# print ("список до перемешивания: " + str(Mylist))
# for i in range(len(Mylist)-1, 0, -1):
#     j = random.randint(0, i + 1)
#     Mylist[i], Mylist[j] = Mylist[j], Mylist[i]
# print ("список после перемешивания: " +  str(Mylist))





#print(f"Список после перемешивания:\n{list}")







