import sqlite3
db = sqlite3.connect('library.db')
qry="update book set name = ? , description=? where upper(name)=upper(?);"
try:
    oldname = input("Enter Book name:")
    name = input("Enter Book correct name:")
    desc = input("Enter Book description:")
    cur = db.cursor()
    cur.execute(qry, (name, desc, oldname))
    db.commit()
    print("book updated successfully")
except:
    print("Book doesn't exist")
    db.rollback()
db.close()