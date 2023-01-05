
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


# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# else:
#  print('Пожалуй')
#  print('хватит )')


# list = [1,5,6,8]
# for i in list:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(5,10,2):
#     print(i)


# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)


# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
# i *= 2
# print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

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


# Стоун (Кирилл): Напишите программу, которая принимает на вход число и 
# проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# num = int(input("Введите число: "))
# if (num%10== 0 or num%15== 0) and (not num%30== 0):
#     print('Выполняется')
# else:
#     print("Не выполняется")

# Стоун (Кирилл): 1. Напишите программу, которая принимает на вход 
# число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

# n=int(input("Введите число: "))
# for i in range(n):
#     print(str(f'{(-3)**i}'),end=" ")
#     print(str(f'{(-3)**i}'),end=", ")


# number = int(input("Введите число: "))
# result = []
# for i in range(number):
#     result.append((-3)**i)
# print(f'Для N = {number}: ', end='')
# print(*result, sep=', ')


# Стоун (Кирилл): 2. Для натурального n создать словарь ключ-значение,
# состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input("Ведите N: "))
# my_dict = {}
# for key in range(1, n+1):
#     my_dict[key] = 3 * key +1 
# print(f'При N = {n}', end = ' ')
# print(my_dict)


# Стоун (Кирилл): Напишите программу, в которой пользователь будет задавать 
# две строки, а программа - определять количество вхождений одной строки в другую.

text = 'Напишите программу, в которой пользователь будет задавать' \
' две строки, а программа - определять количество вхождений одной' \
 'строки в другую.'

search = input('Введите искомый элемент: ')
print(text)
text = text.split()
print(text)
