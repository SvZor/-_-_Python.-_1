"""
Урок 6. Все задачи в одном файле
"""

import random

# ========== ЗАДАЧА 2. Проверка даты ==========

def is_leap_year(year):
    """Проверка на високосный год"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_valid_date(day, month, year):
    """Проверка корректности даты"""
    if not (1 <= month <= 12):
        return False
    
    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    
    if not (1 <= day <= days_in_month[month - 1]):
        return False
    
    return True

def check_date_from_terminal():
    """Запуск проверки даты из терминала (вручную)"""
    date_str = input("Введите дату в формате ДД.ММ.ГГГГ: ")
    parts = date_str.split('.')
    
    if len(parts) != 3:
        print("Неверный формат!")
        return
    
    day, month, year = map(int, parts)
    
    if is_valid_date(day, month, year):
        print(f"Дата {day:02d}.{month:02d}.{year} существует")
    else:
        print(f"Дата {day:02d}.{month:02d}.{year} НЕ существует")

# ========== ЗАДАЧА 3. Проверка 8 ферзей ==========

def are_queens_safe(queens):
    """
    Проверяет, не бьют ли ферзи друг друга
    queens: список из 8 пар (ряд, колонка), от 1 до 8
    """
    rows = set()
    cols = set()
    diag1 = set()  # разность row - col
    diag2 = set()  # сумма row + col
    
    for row, col in queens:
        if row in rows or col in cols:
            return False
        if (row - col) in diag1 or (row + col) in diag2:
            return False
        
        rows.add(row)
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
    
    return True

def check_queens_from_terminal():
    """Ручной ввод координат ферзей"""
    print("Введите координаты 8 ферзей (ряд и колонка от 1 до 8):")
    queens = []
    
    for i in range(8):
        print(f"Ферзь {i+1}:")
        row = int(input("  Ряд (1-8): "))
        col = int(input("  Колонка (1-8): "))
        queens.append((row, col))
    
    if are_queens_safe(queens):
        print("\n✓ Ферзи НЕ бьют друг друга!")
    else:
        print("\n✗ Ферзи бьют друг друга!")

# ========== ЗАДАЧА 4. Генератор успешных расстановок ==========

def generate_random_queen_arrangement():
    """Генерирует случайную расстановку 8 ферзей"""
    rows = list(range(1, 9))
    cols = list(range(1, 9))
    random.shuffle(rows)
    random.shuffle(cols)
    
    return [(rows[i], cols[i]) for i in range(8)]

def find_safe_arrangements(count=4, max_attempts=1000):
    """Находит успешные расстановки"""
    found = []
    attempts = 0
    
    print(f"Поиск {count} расстановок, где ферзи не бьют друг друга...")
    
    while len(found) < count and attempts < max_attempts:
        queens = generate_random_queen_arrangement()
        attempts += 1
        
        if are_queens_safe(queens):
            found.append(queens)
            print(f"  Найдена расстановка #{len(found)} (попытка {attempts})")
            attempts = 0  # Сброс счётчика для следующего поиска
    
    return found

def print_board(queens):
    """Красиво выводит доску с ферзями"""
    print("\n  " + " ".join(str(i) for i in range(1, 9)))
    for row in range(1, 9):
        line = f"{row} "
        for col in range(1, 9):
            if (row, col) in queens:
                line += "♕ "
            else:
                line += "· "
        print(line)
    print()

# ========== ГЛАВНОЕ МЕНЮ ==========

def main():
    while True:
        print("\n" + "=" * 50)
        print("КОНТРОЛЬНАЯ РАБОТА - УРОК 6")
        print("=" * 50)
        print("1. Проверить дату")
        print("2. Проверить 8 ферзей (ввести координаты)")
        print("3. Найти успешные расстановки 8 ферзей")
        print("4. Выйти")
        
        choice = input("\nВыберите действие (1-4): ")
        
        if choice == "1":
            print("\n--- ПРОВЕРКА ДАТЫ ---")
            check_date_from_terminal()
        
        elif choice == "2":
            print("\n--- ПРОВЕРКА 8 ФЕРЗЕЙ ---")
            check_queens_from_terminal()
        
        elif choice == "3":
            print("\n--- ПОИСК УСПЕШНЫХ РАССТАНОВОК ---")
            count = int(input("Сколько расстановок найти (по умолчанию 4): ") or "4")
            arrangements = find_safe_arrangements(count)
            
            if arrangements:
                print(f"\nНайдено {len(arrangements)} расстановок:\n")
                for i, queens in enumerate(arrangements, 1):
                    print(f"Расстановка #{i}: {queens}")
                    print_board(queens)
            else:
                print("Не удалось найти нужное количество расстановок")
        
        elif choice == "4":
            print("\nДо свидания!")
            break
        
        else:
            print("Неверный выбор!")

# Запуск программы
if __name__ == "__main__":
    main()