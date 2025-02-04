# Создаем словарь для хранения информации о заметке
note = {}


# Сбор данных от пользователя
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите содержание заметки: ")
note["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
note["created_date"] = input("Введите дату создания заметки в формате 'день-месяц-год': ")
note["issue_date"] = input("Введите дату изменения заметки в формате 'день-месяц-год': ")


# # Вложенный список для заголовков
#
note["titles"] = []
for i in range(2):
    title = input(f"Введите название заголовока {i + 1}: ")
    note["titles"].append(title)


# Выводим собранные данные
print("\nСобранная информация о заметке:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")

