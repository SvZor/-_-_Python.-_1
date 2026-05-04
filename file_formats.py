"""
Упрощённый пакет для работы с файлами разных форматов (JSON, CSV, Pickle)
"""

import json
import csv
import pickle
import os

# ========== РАБОТА С JSON ==========

def save_json(data, filename):
    """Сохраняет данные в JSON файл"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"✅ Сохранено в {filename}")

def load_json(filename):
    """Загружает данные из JSON файла"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# ========== РАБОТА С CSV ==========

def save_csv(data, filename, fieldnames=None):
    """Сохраняет список словарей в CSV файл"""
    if not data:
        print("❌ Нет данных для сохранения")
        return
    
    if fieldnames is None:
        fieldnames = list(data[0].keys())
    
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"✅ Сохранено в {filename}")

def load_csv(filename):
    """Загружает данные из CSV файла"""
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

# ========== РАБОТА С PICKLE ==========

def save_pickle(data, filename):
    """Сохраняет данные в Pickle файл"""
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    print(f"✅ Сохранено в {filename}")

def load_pickle(filename):
    """Загружает данные из Pickle файла"""
    with open(filename, 'rb') as f:
        return pickle.load(f)

# ========== УНИВЕРСАЛЬНЫЕ ФУНКЦИИ ==========

def save_file(data, filename, format_type):
    """
    Универсальное сохранение в зависимости от расширения файла
    format_type: 'json', 'csv', 'pickle'
    """
    if format_type == 'json':
        save_json(data, filename)
    elif format_type == 'csv':
        save_csv(data, filename)
    elif format_type == 'pickle':
        save_pickle(data, filename)
    else:
        print(f"❌ Неподдерживаемый формат: {format_type}")

def load_file(filename):
    """
    Универсальная загрузка, определяет формат по расширению
    """
    if filename.endswith('.json'):
        return load_json(filename)
    elif filename.endswith('.csv'):
        return load_csv(filename)
    elif filename.endswith('.pkl') or filename.endswith('.pickle'):
        return load_pickle(filename)
    else:
        print(f"❌ Неизвестный формат: {filename}")
        return None


# ========== ДЕМОНСТРАЦИЯ ==========

if __name__ == "__main__":
    print("=" * 60)
    print("ПАКЕТ ДЛЯ РАБОТЫ С ФАЙЛАМИ (JSON, CSV, Pickle)")
    print("=" * 60)
    
    # Тестовые данные
    test_data = [
        {"name": "Иван", "age": 25, "city": "Москва"},
        {"name": "Мария", "age": 30, "city": "СПб"},
        {"name": "Петр", "age": 35, "city": "Казань"}
    ]
    
    print("\n📝 Тестовые данные:")
    for item in test_data:
        print(f"   {item}")
    
    # Сохраняем в разных форматах
    print("\n💾 Сохранение:")
    save_json(test_data, "test_data.json")
    save_csv(test_data, "test_data.csv")
    save_pickle(test_data, "test_data.pkl")
    
    # Загружаем из разных форматов
    print("\n📖 Загрузка:")
    
    json_loaded = load_json("test_data.json")
    print(f"   Из JSON: {len(json_loaded)} записей")
    
    csv_loaded = load_csv("test_data.csv")
    print(f"   Из CSV: {len(csv_loaded)} записей")
    
    pickle_loaded = load_pickle("test_data.pkl")
    print(f"   Из Pickle: {len(pickle_loaded)} записей")
    
    # Универсальная загрузка
    print("\n🔄 Универсальная загрузка (по расширению):")
    data1 = load_file("test_data.json")
    data2 = load_file("test_data.csv")
    data3 = load_file("test_data.pkl")
    
    print(f"   JSON: {data1[0]['name'] if data1 else 'нет'}")
    print(f"   CSV: {data2[0]['name'] if data2 else 'нет'}")
    print(f"   Pickle: {data3[0]['name'] if data3 else 'нет'}")
    
    # Удаляем тестовые файлы
    print("\n🗑️ Удаляем тестовые файлы...")
    for f in ["test_data.json", "test_data.csv", "test_data.pkl"]:
        if os.path.exists(f):
            os.remove(f)
    
    print("\n✅ Демонстрация завершена!")