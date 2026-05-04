"""
Урок 8. Рекурсивный обход директории с сохранением в JSON, CSV, Pickle
"""

import os
import json
import csv
import pickle

def get_directory_size(directory):
    """
    Рекурсивно вычисляет размер директории (сумму всех файлов внутри)
    Возвращает размер в байтах
    """
    total_size = 0
    
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            
            if os.path.isfile(item_path):
                total_size += os.path.getsize(item_path)
            elif os.path.isdir(item_path):
                total_size += get_directory_size(item_path)
    except PermissionError:
        # Если нет доступа к папке, пропускаем
        pass
    
    return total_size


def scan_directory(root_dir):
    """
    Рекурсивно обходит директорию и собирает информацию обо всех объектах
    Возвращает список словарей с информацией
    """
    results = []
    
    # Проходим по всем элементам в текущей директории
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        
        # Определяем тип объекта
        if os.path.isfile(item_path):
            item_type = "file"
            size = os.path.getsize(item_path)
        elif os.path.isdir(item_path):
            item_type = "directory"
            size = get_directory_size(item_path)  # Полный размер директории
        else:
            continue  # Пропускаем ссылки и другие объекты
        
        # Сохраняем информацию
        results.append({
            "name": item,
            "path": os.path.abspath(item_path),
            "parent_dir": os.path.abspath(root_dir),
            "type": item_type,
            "size_bytes": size
        })
        
        # Если это директория, рекурсивно обходим её
        if os.path.isdir(item_path):
            results.extend(scan_directory(item_path))
    
    return results


def save_to_json(data, filename="scan_result.json"):
    """Сохраняет данные в JSON файл"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"✅ Сохранено в JSON: {filename}")


def save_to_csv(data, filename="scan_result.csv"):
    """Сохраняет данные в CSV файл"""
    if not data:
        print("❌ Нет данных для сохранения в CSV")
        return
    
    # Поля для CSV
    fieldnames = ["name", "path", "parent_dir", "type", "size_bytes"]
    
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"✅ Сохранено в CSV: {filename}")


def save_to_pickle(data, filename="scan_result.pkl"):
    """Сохраняет данные в Pickle файл"""
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    print(f"✅ Сохранено в Pickle: {filename}")


def save_results(data, base_name="scan_result"):
    """Сохраняет данные во всех трёх форматах"""
    save_to_json(data, f"{base_name}.json")
    save_to_csv(data, f"{base_name}.csv")
    save_to_pickle(data, f"{base_name}.pkl")


def print_summary(data):
    """Выводит краткую сводку о результатах сканирования"""
    print("\n" + "=" * 60)
    print("📊 СВОДКА РЕЗУЛЬТАТОВ")
    print("=" * 60)
    
    files = [item for item in data if item["type"] == "file"]
    dirs = [item for item in data if item["type"] == "directory"]
    
    total_size = sum(item["size_bytes"] for item in data)
    
    print(f"📁 Всего объектов: {len(data)}")
    print(f"📄 Файлов: {len(files)}")
    print(f"📂 Директорий: {len(dirs)}")
    print(f"💾 Общий размер: {total_size / 1024 / 1024:.2f} МБ ({total_size} байт)")
    
    print("\n📋 Первые 5 объектов:")
    for i, item in enumerate(data[:5], 1):
        size_str = f"{item['size_bytes']} байт"
        if item['size_bytes'] > 1024:
            size_str = f"{item['size_bytes'] / 1024:.1f} КБ"
        print(f"   {i}. {item['name']} ({item['type']}) - {size_str}")


def load_and_check_examples():
    """Примеры загрузки данных из разных форматов"""
    print("\n" + "=" * 60)
    print("📖 ПРИМЕРЫ ЗАГРУЗКИ ДАННЫХ")
    print("=" * 60)
    
    # Загрузка из JSON
    try:
        with open("scan_result.json", 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        print(f"✅ Из JSON загружено {len(json_data)} объектов")
        print(f"   Первый объект: {json_data[0]['name']}")
    except FileNotFoundError:
        print("❌ Файл scan_result.json не найден")
    
    # Загрузка из CSV
    try:
        with open("scan_result.csv", 'r', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            csv_data = list(csv_reader)
        print(f"✅ Из CSV загружено {len(csv_data)} объектов")
        print(f"   Первый объект: {csv_data[0]['name']}")
    except FileNotFoundError:
        print("❌ Файл scan_result.csv не найден")
    
    # Загрузка из Pickle
    try:
        with open("scan_result.pkl", 'rb') as f:
            pickle_data = pickle.load(f)
        print(f"✅ Из Pickle загружено {len(pickle_data)} объектов")
        print(f"   Первый объект: {pickle_data[0]['name']}")
    except FileNotFoundError:
        print("❌ Файл scan_result.pkl не найден")


# ========== ОСНОВНАЯ ПРОГРАММА ==========

if __name__ == "__main__":
    print("=" * 60)
    print("🔍 СКАНЕР ДИРЕКТОРИЙ (рекурсивный обход)")
    print("=" * 60)
    
    # Получаем директорию для сканирования
    scan_path = input("\n📁 Введите путь для сканирования (Enter для текущей папки): ").strip()
    
    if not scan_path:
        scan_path = "."
    
    # Проверяем, существует ли директория
    if not os.path.exists(scan_path):
        print(f"❌ Директория '{scan_path}' не существует!")
        exit(1)
    
    if not os.path.isdir(scan_path):
        print(f"❌ '{scan_path}' не является директорией!")
        exit(1)
    
    print(f"\n🔍 Сканирую: {os.path.abspath(scan_path)}")
    print("⏳ Это может занять некоторое время...")
    
    # Сканируем директорию
    results = scan_directory(scan_path)
    
    if not results:
        print("❌ Не найдено объектов для сканирования")
        exit(1)
    
    # Показываем сводку
    print_summary(results)
    
    # Спрашиваем, нужно ли сохранить
    save_choice = input("\n💾 Сохранить результаты в JSON, CSV и Pickle? (y/n): ")
    
    if save_choice.lower() == 'y':
        # Определяем имя файла на основе пути
        base_name = "scan_result"
        if scan_path != ".":
            # Берём имя папки
            safe_name = os.path.basename(os.path.abspath(scan_path))
            if safe_name:
                base_name = f"scan_{safe_name}"
        
        save_results(results, base_name)
        
        # Показываем примеры загрузки
        load_and_check_examples()
    
    print("\n✅ Работа программы завершена!")