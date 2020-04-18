from database import Database

conn = Database()

print("Database application")
while True:
    print('select option')
    print('1.add')
    print('2.View')
    print('3.Exit')
    option = input('Enter number :::->')
    if option == '1':
        print("Add data to Database")
        name = input("Name:")
        email = input("Email:")
        password = input("password :")
        conn.add(name, email, password)
        print("Done")
    elif option == '2':
        data = conn.view()
        for record in data:
            print(record)
    else:
        print('bye')
        break

data = conn.run('''select * from detail where name = "hime" and pwd = "qwerty123";''')
for record in data:
    print(record)