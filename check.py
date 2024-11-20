import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Registration Data:")
for row in rows:
    print(row)

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("\nLogin Data:")
for row in rows:
    print(row)

conn.close()
