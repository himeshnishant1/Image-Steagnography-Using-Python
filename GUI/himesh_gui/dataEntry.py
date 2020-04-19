from database import Database

conn = Database()

print("Database application")

data = conn.run('''select * from detail where name = "himesh" and pwd = "qwerty123";''')
for record in data:
    print(record)
    print(record[0])