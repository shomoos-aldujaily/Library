import sqlite3
db=sqlite3.connect('library.db')
qry="DELETE from book where upper(name)=upper(?);"
try:
    book = input("Enter Book name:")
    cur=db.cursor()
    cur.execute(qry, (book))
    db.commit()
    print("record deleted successfully")
except:
    print("error in operation")
    db.rollback()
db.close()