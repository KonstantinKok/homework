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

connection.commit()
connection.close()
