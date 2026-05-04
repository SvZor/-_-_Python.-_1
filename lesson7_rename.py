"""
Урок 7. Групповое переименование файлов
Простое решение без пакетов
"""

import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    """
    Групповое переименование файлов
    
    Параметры:
    - desired_name: желаемое конечное имя файлов
    - num_digits: количество цифр в порядковом номере
    - source_ext: расширение исходного файла (без точки, например "txt")
    - target_ext: расширение конечного файла (без точки, например "csv")
    - name_range: диапазон сохраняемого имени [начало, конец] (например [3, 6])
    """
    
    # Получаем список ВСЕХ файлов в текущей папке
    all_files = os.listdir('.')
    
    # Отбираем только нужные файлы (с нужным расширением)
    files_to_rename = []
    for file in all_files:
        if os.path.isfile(file) and file.endswith('.' + source_ext):
            files_to_rename.append(file)
    
    if not files_to_rename:
        print(f"❌ Файлы с расширением .{source_ext} не найдены!")
        return
    
    # Сортируем для порядка
    files_to_rename.sort()
    
    # Формируем шаблон для номера (например 3 цифры -> "001", "002"...)
    num_template = "{:0" + str(num_digits) + "d}"
    
    counter = 1
    
    print(f"Найдено файлов: {len(files_to_rename)}")
    print("-" * 50)
    
    for old_name in files_to_rename:
        # Убираем расширение из имени файла
        name_without_ext = old_name[:-(len(source_ext) + 1)]
        
        # Начинаем формировать новое имя
        new_name = ""
        
        # Если задан диапазон, берём часть из оригинального имени
        if name_range is not None:
            start, end = name_range
            # Проверяем, что имени хватает для среза
            if len(name_without_ext) >= end:
                # Вырезаем символы с start по end (в Python индексы с 0)
                old_part = name_without_ext[start-1:end]
                new_name += old_part
        
        # Добавляем желаемое имя
        new_name += desired_name
        
        # Добавляем порядковый номер
        new_name += num_template.format(counter)
        
        # Добавляем новое расширение
        new_name += "." + target_ext
        
        # Переименовываем
        os.rename(old_name, new_name)
        print(f"✅ {old_name}  ->  {new_name}")
        
        counter += 1
    
    print("-" * 50)
    print(f"✅ Переименовано {counter - 1} файлов!")


# ========== ТЕСТОВАЯ ФУНКЦИЯ ==========

def create_test_files():
    """Создаёт тестовые файлы в текущей папке"""
    print("\n📁 Создаю тестовые файлы...")
    
    for i in range(1, 6):
        filename = f"document_{i}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Тестовый файл номер {i}")
        print(f"   ✅ Создан: {filename}")


def show_current_txt_files():
    """Показывает все .txt файлы в текущей папке"""
    print("\n📄 Текущие .txt файлы в папке:")
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt')]
    
    if not files:
        print("   ❌ Нет .txt файлов")
    else:
        for f in files:
            print(f"   📄 {f}")


# ========== ГЛАВНАЯ ПРОГРАММА ==========

if __name__ == "__main__":
    print("=" * 60)
    print("ГРУППОВОЕ ПЕРЕИМЕНОВАНИЕ ФАЙЛОВ")
    print("=" * 60)
    
    # Показываем текущие файлы
    show_current_txt_files()
    
    # Спрашиваем, нужно ли создать тестовые файлы
    if not any(f.endswith('.txt') for f in os.listdir('.')):
        create = input("\nНет .txt файлов. Создать тестовые? (y/n): ")
        if create.lower() == 'y':
            create_test_files()
            show_current_txt_files()
    
    print("\n" + "=" * 60)
    
    # ВАРИАНТ 1: Простое переименование
    print("\n📌 ВАРИАНТ 1: Простое переименование")
    print("   (все .txt -> .csv с номером)")
    print("-" * 60)
    
    rename_files(
        desired_name="_new_",
        num_digits=3,
        source_ext="txt",
        target_ext="csv"
    )
    
    # Возвращаем обратно для следующего примера
    print("\n🔄 Возвращаю обратно в .txt...")
    for file in os.listdir('.'):
        if file.endswith('.csv'):
            os.rename(file, file.replace('.csv', '.txt'))
    
    show_current_txt_files()
    
    print("\n" + "=" * 60)
    
    # ВАРИАНТ 2: С сохранением части оригинального имени
    print("\n📌 ВАРИАНТ 2: С сохранением части имени [1,4]")
    print("   (берём символы 1-4 из оригинала + _doc + номер)")
    print("-" * 60)
    
    rename_files(
        desired_name="_doc",
        num_digits=2,
        source_ext="txt",
        target_ext="md",
        name_range=[1, 4]  # берём первые 4 символа (с 1 по 4)
    )
    
    print("\n" + "=" * 60)
    print("✅ Работа программы завершена!")