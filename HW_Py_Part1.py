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

# # Задача 4. Сбор рюкзака (вещи для похода)

# # Словарь: вещь -> масса (в кг)
# items = {
#     "палатка": 3,
#     "спальник": 1.5,
#     "коврик": 0.5,
#     "котелок": 0.8,
#     "еда": 2,
#     "вода": 1.5,
#     "аптечка": 0.3,
#     "фонарик": 0.2,
#     "спички": 0.05,
#     "ножик": 0.1,
#     "топор": 1.2,
#     "смена одежды": 1,
#     "дождевик": 0.4
# }

# max_capacity = 5  # Максимальная грузоподъёмность рюкзака

# # Жадный алгоритм (берём самое нужное/лёгкое)
# print(f"Грузоподъёмность рюкзака: {max_capacity} кг\n")

# remaining_capacity = max_capacity
# backpack = []

# # Сортируем вещи по весу (от лёгких к тяжёлым)
# sorted_items = sorted(items.items(), key=lambda x: x[1])

# for item, weight in sorted_items:
#     if weight <= remaining_capacity:
#         backpack.append(item)
#         remaining_capacity -= weight
#         print(f"Добавлено: {item} ({weight} кг), осталось места: {remaining_capacity:.2f} кг")

# print(f"\nВ рюкзак поместилось {len(backpack)} вещей: {', '.join(backpack)}")
# print(f"Общий вес: {max_capacity - remaining_capacity:.2f} кг")

# # Семинар 4
# # Задача 1. Транспонирование матрицы

# def transpose_matrix(matrix):
#     """
#     Транспонирует матрицу (меняет строки и столбцы местами)
#     """
#     # Получаем количество строк и столбцов исходной матрицы
#     rows = len(matrix)
#     cols = len(matrix[0])
    
#     # Создаём новую матрицу с размерами cols x rows, заполненную нулями
#     result = []
#     for i in range(cols):
#         result.append([0] * rows)
    
#     # Заполняем транспонированную матрицу
#     for i in range(rows):
#         for j in range(cols):
#             result[j][i] = matrix[i][j]
    
#     return result

# # Пример использования
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# print("Исходная матрица:")
# for row in matrix:
#     print(row)

# transposed = transpose_matrix(matrix)

# print("\nТранспонированная матрица:")
# for row in transposed:
#     print(row)

# # Задача 2. Функция с ключевыми параметрами

# def make_dict(**kwargs):
#     """
#     Принимает ключевые параметры и возвращает словарь,
#     где ключ — значение аргумента, а значение — имя аргумента
#     """
#     result = {}
    
#     for key, value in kwargs.items():
#         # Проверяем, хешируемый ли ключ (можно ли его использовать как ключ словаря)
#         try:
#             # Пробуем создать словарь с этим ключом
#             test_dict = {value: 1}
#             result[value] = key
#         except TypeError:
#             # Если не получилось (ключ не хешируемый), используем строковое представление
#             result[str(value)] = key
    
#     return result

# # Пример использования
# result = make_dict(a=10, b="hello", c=[1, 2, 3], d=(4, 5), e={1:2})

# print("Результат:")
# for k, v in result.items():
#     print(f"{k} : {v}")

# #  Задача 3. Банкомат с функциями
# # Список для хранения всех операций
# operations = []

# def show_balance(balance):
#     """Показывает текущий баланс"""
#     print(f"\nВаш баланс: {balance} руб.")
#     operations.append(f"Проверка баланса: {balance} руб.")

# def deposit(balance):
#     """Пополнение счёта"""
#     try:
#         amount = int(input("Введите сумму для пополнения: "))
        
#         if amount <= 0:
#             print("Сумма должна быть положительной!")
#             return balance
        
#         # Начисляем проценты (3% от суммы пополнения, но не более 600 руб.)
#         percent = amount * 0.03
#         if percent > 600:
#             percent = 600
        
#         balance += amount + percent
#         print(f"Внесено {amount} руб. Начислено {percent:.2f} руб. процентов")
#         operations.append(f"Пополнение: +{amount} руб. (+{percent:.2f} руб. проценты)")
        
#         return balance
#     except ValueError:
#         print("Ошибка: нужно ввести число!")
#         return balance

# def withdraw(balance):
#     """Снятие денег"""
#     try:
#         amount = int(input("Введите сумму для снятия: "))
        
#         if amount <= 0:
#             print("Сумма должна быть положительной!")
#             return balance
        
#         # Комиссия 1.5% от суммы снятия, минимум 30 руб, максимум 600 руб
#         commission = amount * 0.015
        
#         if commission < 30:
#             commission = 30
#         elif commission > 600:
#             commission = 600
        
#         total_to_withdraw = amount + commission
        
#         if total_to_withdraw > balance:
#             print(f"Недостаточно средств! Нужно {total_to_withdraw:.2f} руб. (включая комиссию {commission:.2f} руб.)")
#             return balance
        
#         balance -= total_to_withdraw
#         print(f"Снято {amount} руб. Комиссия: {commission:.2f} руб.")
#         operations.append(f"Снятие: -{amount} руб. (-{commission:.2f} руб. комиссия)")
        
#         return balance
#     except ValueError:
#         print("Ошибка: нужно ввести число!")
#         return balance

# def show_operations():
#     """Показывает историю операций"""
#     if not operations:
#         print("\nИстория операций пуста")
#         return
    
#     print("\n=== ИСТОРИЯ ОПЕРАЦИЙ ===")
#     for i, operation in enumerate(operations, 1):
#         print(f"{i}. {operation}")

# # Основная программа
# def main():
#     balance = 0
#     print("=" * 40)
#     print("ДОБРО ПОЖАЛОВАТЬ В БАНКОМАТ")
#     print("=" * 40)
    
#     while True:
#         print(f"\n--- Баланс: {balance} руб. ---")
#         print("1. Пополнить счёт")
#         print("2. Снять деньги")
#         print("3. Показать историю операций")
#         print("4. Выйти")
        
#         choice = input("Выберите действие (1-4): ")
        
#         if choice == "1":
#             balance = deposit(balance)
#         elif choice == "2":
#             balance = withdraw(balance)
#         elif choice == "3":
#             show_operations()
#         elif choice == "4":
#             print("\nСпасибо за пользование банкоматом!")
#             operations.append("Завершение работы")
#             break
#         else:
#             print("Неверный выбор! Попробуйте снова.")

# # Запуск программы
# if __name__ == "__main__":
#     main()

# # Семинар 5
# #  Задача 2. Разбор пути к файлу

# def parse_file_path(file_path):
#     """
#     Принимает абсолютный путь до файла и возвращает кортеж:
#     (путь, имя файла, расширение файла)
#     """
#     # Находим последний слэш (разделитель папок)
#     last_slash = file_path.rfind('/')
#     last_backslash = file_path.rfind('\\')
    
#     # Берём тот разделитель, который есть (или -1 если ни одного)
#     separator = max(last_slash, last_backslash)
    
#     if separator == -1:
#         # Если нет разделителей, значит путь не указан
#         path = ""
#         filename_with_ext = file_path
#     else:
#         # Отделяем путь от остального
#         path = file_path[:separator]
#         filename_with_ext = file_path[separator + 1:]
    
#     # Находим последнюю точку (расширение файла)
#     last_dot = filename_with_ext.rfind('.')
    
#     if last_dot == -1:
#         # Если нет точки, значит расширения нет
#         filename = filename_with_ext
#         extension = ""
#     else:
#         # Отделяем имя файла от расширения
#         filename = filename_with_ext[:last_dot]
#         extension = filename_with_ext[last_dot + 1:]
    
#     return (path, filename, extension)

# # Пример использования
# path1 = "C:/Users/Максим/Documents/example.py"
# path2 = "D:\\Projects\\data\\report.txt"
# path3 = "script.js"

# print(parse_file_path(path1))
# print(parse_file_path(path2))
# print(parse_file_path(path3))

# # Задача 3. Однострочный генератор словаря с премией

# # Исходные данные
# names = ["Иван", "Петр", "Сидор"]
# salaries = [50000, 60000, 55000]
# bonuses = ["10.25%", "15.5%", "8.75%"]

# # Однострочный генератор словаря
# result = {name: salary * float(bonus.strip('%')) / 100 for name, salary, bonus in zip(names, salaries, bonuses)}

# print(result)

# # Задача 4. Генератор чисел Фибоначчи

# def fibonacci_generator(count):
#     """
#     Генератор чисел Фибоначчи
#     count - сколько чисел нужно сгенерировать
#     """
#     a, b = 0, 1
#     for _ in range(count):
#         yield a
#         a, b = b, a + b

# # Пример использования
# print("Первые 10 чисел Фибоначчи:")
# for num in fibonacci_generator(10):
#     print(num, end=" ")


