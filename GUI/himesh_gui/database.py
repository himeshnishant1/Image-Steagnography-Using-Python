import sqlite3

class Database:

    def __init__(self,name='test.sqlite3'):
        self.db = sqlite3.connect(name)

    def run(self,query):
        try:
            result = self.db.execute(query)
            self.db.commit()
            return result
        except Exception as e:
            print(e)

