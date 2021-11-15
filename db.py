import sqlite3

# from part_manager import update_item
class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY,part text)")
        self.conn.commit()
    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        # rows=self.cur.fetchall()
        rows=[]
        for i in self.cur.fetchall():
            rows.append(i)
        return rows
    def insert(self,part):
        self.cur.execute("INSERT INTO parts VALUES (NULL ,?)",(part,))
        self.conn.commit()
    def remove(self,id):
        self.cur.execute("DELETE FROM parts WHERE id=?",(id,))
        self.conn.commit()
    def update(self,id,part):
        self.cur.execute("UPDATE parts SET part=? WHERE id=?" ,(part,id))
        self.conn.commit()
    def __del__(self):
        self.conn.close()
db=Database('store.db')
# db.insert("first task")
# db.insert("second task")
# db.insert("third task")
# db.insert("fourth task")

