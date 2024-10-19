import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance TEXT NOT NULL
)
''')

# Удалите из базы данных not_telegram.db запись с id = 6

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

#Подсчитать общее количество записей.
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print(f"Общее колличество стало: {total_users}")

#Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
balance_sum = cursor.fetchone()[0]
print(f"Общая сумма баланса стала:) {balance_sum} руб.")

#Вывести в консоль средний баланс всех пользователя.
print(f"Средний баланс пользователей: {int(balance_sum / total_users)} руб.")

connection.commit()
connection.close()