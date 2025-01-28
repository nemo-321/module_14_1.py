import sqlite3

# # Создание базы данных и подключения к ней
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
# Создание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(10):
    cursor.execute("INSERT INTO Users(username,email,age,balance) VALUES (?,?,?,?)",
                   (f"User{i + 1}", f"example{i + 1}@gmail.com", f"{(i + 1) * 10}", "1000"))
# Обновление balance
cursor.execute("UPDATE Users SET balance = ? WHERE id%2 != ?", (500, 0))
# ▎Удаление записей
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
# Выборка записей
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))

users = cursor.fetchall()

for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст:{user[2]} | Баланс: {user[3]}")
# Закрытие соединения
connection.commit()
connection.close()
