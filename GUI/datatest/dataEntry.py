from database import Database

db = Database()

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
        db.add(name, email,pWd)
        print("Done")
    elif option == '2':
        data = db.view()
        for record in data:
            print(record)
    else:
        print('bye')
        break
