username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'ДД-ММ-ГГГГ': ")
issue_date = input("Введите дату истечения заметки в формате 'ДД-ММ-ГГГГ': ")


# Выводим введенные данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
#temp_created_date = created_date[0:5]
#print("Дата создания заметки:", temp_created_date)
print("Дата создания заметки:", created_date[0:5])
#temp_issue_date = issue_date[0:5]
#print("Дата истечения заметки:", temp_issue_date)
print("Дата истечения заметки:", issue_date[0:5])

