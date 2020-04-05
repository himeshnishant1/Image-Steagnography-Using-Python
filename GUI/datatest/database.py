import sqlite3

class Database:

    def __init__(self,name='D://db.sqlite3'):
        self.db = sqlite3.connect(name)
        self.create_table()

    def run(self,query):
        try:
            result = self.db.execute(query)
            self.db.commit()
            return result
        except Exception as e:
            print(e)

    def create_table(self):
        query = '''
            create table detail (
                id integer primary key autoincrement,
                name TEXT,
                email TEXT,
                pwd TEXT,
            )
        '''
        return self.run(query)

    def add(self,name,price,qty):
        query = f'''
            insert into detail values(
                null,
                '{name}',
                '{email}',
                '{pwd}'
            )
        '''
        return self.run(query)

    def view(self):
        query = '''
            select * from detail
        '''
        data = self.run(query)
        if data:
            return data.fetchall()
        else:
            print("no data found")

