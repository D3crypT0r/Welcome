import sqlite3

conn = sqlite3.connect('yourdb.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM "yourtable")
rows = cursor.fetchall()

print("Registration Data:")
for row in rows:
    print(row)

cursor.execute("SELECT * FROM "yourtable")
rows = cursor.fetchall()

print("\nLogin Data:")
for row in rows:
    print(row)

conn.close()
