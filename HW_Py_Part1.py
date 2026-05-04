# # Семинар 1
# # Задача 2. Треугольник.
# # Ввод сторон треугольника
# a = float(input("Введите сторону a: "))
# b = float(input("Введите сторону b: "))
# c = float(input("Введите сторону c: "))

# # Проверка существования треугольника
# if a + b > c and a + c > b and b + c > a:
#     print("Треугольник существует")
    
#     # Определение типа треугольника
#     if a == b == c:
#         print("Треугольник равносторонний")
#     elif a == b or a == c or b == c:
#         print("Треугольник равнобедренный")
#     else:
#         print("Треугольник разносторонний")
# else:
#     print("Треугольник не существует")

# # Задача 3. Простое или составное число.

# # Запрашиваем число
# num = int(input("Введите число от 2 до 100 000: "))

# # Проверка ограничений
# if num < 2 or num > 100000:
#     print("Ошибка: число должно быть от 2 до 100 000")
# else:
#     # Флаг, простое ли число (изначально считаем, что простое)
#     is_prime = True
    
#     # Проверяем делители от 2 до num-1
#     # Достаточно проверить до квадратного корня, но для простоты оставим так
#     for i in range(2, num):
#         if num % i == 0:  # Если делится без остатка
#             is_prime = False
#             break  # Можно прервать, так как уже нашли делитель
    
#     # Вывод результата
#     if is_prime:
#         print(f"{num} — простое число")
#     else:
#         print(f"{num} — составное число")

# # Задача 4. Угадай число за 10 попыток

# from random import randint

# LOWER_LIMIT = 0
# UPPER_LIMIT = 1000

# # Загадываем число
# secret_num = randint(LOWER_LIMIT, UPPER_LIMIT)

# print("Я загадал число от 0 до 1000. Попробуй угадать за 10 попыток!")

# # Счётчик попыток
# attempts = 10

# while attempts > 0:
#     guess = int(input(f"Осталось попыток: {attempts}. Твоё число: "))
    
#     if guess < secret_num:
#         print("Больше!")
#     elif guess > secret_num:
#         print("Меньше!")
#     else:
#         print(f"Поздравляю! Ты угадал число {secret_num}!")
#         break  # Выходим из цикла, если угадали
    
#     attempts -= 1  # Уменьшаем количество попыток

# # Если попытки закончились
# if attempts == 0:
#     print(f"Попытки закончились. Я загадал число {secret_num}.")

# # Семинар 2.
# # Задача 2. Получение шестнадцатеричного представления числа

# # Получаем целое число от пользователя
# num = int(input("Введите целое число: "))

# # Запоминаем исходное число для проверки
# original_num = num

# # Обрабатываем отрицательные числа (для красоты)
# is_negative = False
# if num < 0:
#     is_negative = True
#     num = -num

# # Шестнадцатеричная система: цифры 0-9 и A-F
# hex_digits = "0123456789ABCDEF"

# # Переменная для результата (пока пустая строка)
# hex_result = ""

# # Особый случай: если число 0
# if num == 0:
#     hex_result = "0"
# else:
#     # Переводим число в 16-ю систему
#     while num > 0:
#         remainder = num % 16  # Остаток от деления на 16
#         hex_result = hex_digits[remainder] + hex_result  # Добавляем цифру в начало
#         num = num // 16  # Целочисленное деление на 16

# # Добавляем знак минус для отрицательных чисел
# if is_negative:
#     hex_result = "-" + hex_result

# # Проверка с помощью встроенной функции hex
# print(f"Моё преобразование: {hex_result}")
# print(f"Проверка через hex(): {hex(original_num)}")
# print(f"Результаты совпадают: {hex_result == hex(original_num)}")


# # Задача 3. Сумма и произведение дробей

# # Получаем две дроби от пользователя
# frac1 = input("Введите первую дробь (в формате a/b): ")
# frac2 = input("Введите вторую дробь (в формате a/b): ")

# # Разбираем первую дробь
# numerator1, denominator1 = map(int, frac1.split('/'))

# # Разбираем вторую дробь
# numerator2, denominator2 = map(int, frac2.split('/'))

# # Функция для нахождения наибольшего общего делителя (алгоритм Евклида)
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return abs(a)

# # Функция для сокращения дроби
# def reduce_fraction(numerator, denominator):
#     common_divisor = gcd(numerator, denominator)
#     return numerator // common_divisor, denominator // common_divisor

# # 1. СУММА дробей
# # Приводим к общему знаменателю
# sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
# sum_denominator = denominator1 * denominator2

# # Сокращаем результат
# sum_numerator, sum_denominator = reduce_fraction(sum_numerator, sum_denominator)

# # 2. ПРОИЗВЕДЕНИЕ дробей
# prod_numerator = numerator1 * numerator2
# prod_denominator = denominator1 * denominator2

# # Сокращаем результат
# prod_numerator, prod_denominator = reduce_fraction(prod_numerator, prod_denominator)

# # Вывод результатов
# print(f"\nСумма: {frac1} + {frac2} = {sum_numerator}/{sum_denominator}")
# print(f"Произведение: {frac1} * {frac2} = {prod_numerator}/{prod_denominator}")

# # ПРОВЕРКА через модуль fractions
# from fractions import Fraction

# f1 = Fraction(numerator1, denominator1)
# f2 = Fraction(numerator2, denominator2)

# print(f"\nПроверка через fractions:")
# print(f"Сумма: {f1} + {f2} = {f1 + f2}")
# print(f"Произведение: {f1} * {f2} = {f1 * f2}")


# # Семинар 3.
# # Задача 2. Поиск дублирующихся элементов

# # Дан список повторяющихся элементов
# my_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 1, 8, 9, 2, 5]

# # Находим дубликаты
# seen = set()      # Множество для уже встреченных элементов
# duplicates = set() # Множество для дубликатов

# for item in my_list:
#     if item in seen:
#         duplicates.add(item)  # Если уже встречали - добавляем в дубликаты
#     else:
#         seen.add(item)        # Если первый раз - запоминаем

# # Превращаем множество в список
# result = list(duplicates)

# print(f"Исходный список: {my_list}")
# print(f"Элементы, которые повторяются: {result}")

# # Задача 3. 10 самых частых слов в тексте

# # Возьмём текст из документации Python (первые строки)
# text = """
# Python is an easy to learn, powerful programming language. It has efficient high-level data structures 
# and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic 
# typing, together with its interpreted nature, make it an ideal language for scripting and rapid application 
# development in many areas on most platforms. The Python interpreter and the extensive standard library are 
# freely available in source or binary form for all major platforms from the Python web site, 
# https://www.python.org/, and may be freely distributed. The same site also contains distributions of 
# and pointers to many free third party Python modules, programs and tools, and additional documentation.
# """

# # Приводим к нижнему регистру
# text_lower = text.lower()

# # Заменяем знаки препинания на пробелы
# punctuation = ".,!?;:-()[]{}'\"«»–—"
# for punct in punctuation:
#     text_lower = text_lower.replace(punct, ' ')

# # Разбиваем текст на слова
# words = text_lower.split()

# # Считаем частоту каждого слова
# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# # Сортируем слова по частоте (от большего к меньшему)
# sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# # Берём 10 самых частых
# top_10 = sorted_words[:10]

# print("10 самых частых слов в тексте:")
# print("Слово".ljust(15), "Количество")
# print("-" * 25)
# for word, count in top_10:
#     print(word.ljust(15), count)

# Задача 4. Сбор рюкзака (вещи для похода)

# Словарь: вещь -> масса (в кг)
items = {
    "палатка": 3,
    "спальник": 1.5,
    "коврик": 0.5,
    "котелок": 0.8,
    "еда": 2,
    "вода": 1.5,
    "аптечка": 0.3,
    "фонарик": 0.2,
    "спички": 0.05,
    "ножик": 0.1,
    "топор": 1.2,
    "смена одежды": 1,
    "дождевик": 0.4
}

max_capacity = 5  # Максимальная грузоподъёмность рюкзака

# Жадный алгоритм (берём самое нужное/лёгкое)
print(f"Грузоподъёмность рюкзака: {max_capacity} кг\n")

remaining_capacity = max_capacity
backpack = []

# Сортируем вещи по весу (от лёгких к тяжёлым)
sorted_items = sorted(items.items(), key=lambda x: x[1])

for item, weight in sorted_items:
    if weight <= remaining_capacity:
        backpack.append(item)
        remaining_capacity -= weight
        print(f"Добавлено: {item} ({weight} кг), осталось места: {remaining_capacity:.2f} кг")

print(f"\nВ рюкзак поместилось {len(backpack)} вещей: {', '.join(backpack)}")
print(f"Общий вес: {max_capacity - remaining_capacity:.2f} кг")