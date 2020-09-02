import sqlite3
db=sqlite3.connect('library.db')
sql="SELECT * from author;"
cur=db.cursor()
cur.execute(sql)
while True:
    record=cur.fetchone()
    if record==None:
        break
    print (record)
db.close()
