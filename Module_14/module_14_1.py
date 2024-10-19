import sqlite3
import random

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

#cursor.execute('CREATE INDEX idx_email ON Users (email)')

# for i in range(10):
#     cursor.execute(" INSERT INTO Users(username, email, age, balance) VALUES(?,?,?,?)", (f"newuser{i}", f"ex@gmail.com{i}", str(random.randint(18,60)),1000))

cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500,1, ))
cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500,3))
cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500,5))
cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500,7))
cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500,9))


cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))

results1 = cursor.fetchall()
for row in results1:
  print(row)

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
