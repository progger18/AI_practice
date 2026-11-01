import os
import psutil

# 1. Процессор (CPU)
cpu_count_logical = psutil.cpu_count()  # Логические ядра
cpu_count_physical = psutil.cpu_count(logical=False)  # Физические ядра
# percpu=True покажет загрузку каждого ядра отдельно
cpu_usage = psutil.cpu_percent(interval=1)

print("--- ПРОЦЕССОР ---")
print(f"Ядер (физических/логических): {cpu_count_physical}/{cpu_count_logical}")
print(f"Текущая общая загрузка CPU: {cpu_usage}%")

# 2. Оперативная память (RAM)
ram = psutil.virtual_memory()
# Переводим байты в гигабайты
bytes_to_gb = 1024**3

print("\n--- ОПЕРАТИВНАЯ ПАМЯТЬ ---")
print(f"Всего памяти: {ram.total / bytes_to_gb:.2f} GB")
print(f"Использовано: {ram.used / bytes_to_gb:.2f} GB")
print(f"Свободно: {ram.available / bytes_to_gb:.2f} GB")
print(f"Загрузка RAM: {ram.percent}%")

# 3. Дисковая подсистема
# На Windows можно указать конкретный диск, например 'C:\\'
disk = psutil.disk_usage("/")

print("\n--- ДИСКОВАЯ ПАМЯТЬ ---")
print(f"Всего на диске: {disk.total / bytes_to_gb:.2f} GB")
print(f"Использовано: {disk.used / bytes_to_gb:.2f} GB")
print(f"Свободно: {disk.free / bytes_to_gb:.2f} GB")
print(f"Загрузка диска: {disk.percent}%")

# 4. Сетевой трафик (с момента включения ПК)
net_io = psutil.net_io_counters()

print("\n--- СЕТЬ ---")
print(f"Отправлено: {net_io.bytes_sent / bytes_to_gb:.4f} GB")
print(f"Получено: {net_io.bytes_recv / bytes_to_gb:.4f} GB")

psutil.on