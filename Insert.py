import sqlite3
db=sqlite3.connect('library.db')
qry="insert into BOOK (name, description) values(?,?);"
bookid=0
try:
    cur=db.cursor()
    name=input("Enter Book Name")
    desc=input("Enter Book Description")

    cur.execute(qry,(name, desc))
    db.commit()
    print ("one record added successfully")
except:
    print ("error in operation")
    db.rollback()

bookid=cur.lastrowid
print("new book id:",bookid)
firstname=input("Enter Author First Name")
lastname=input("Enter Author Last Name")

qry="select authorid from AUTHOR where upper(firstname) = upper(?) and upper(lastname)=upper(?);"

cur.execute(qry,(firstname, lastname))

cur1=db.cursor()
print(cur.fetchone()==None)
if cur.fetchone() != None:
    qry="insert into BOOK_author(bookid,authorid)  values(?,?);"
    authid=cur.fetchone()[0]
    print("new auth id:",authid)
    cur1.execute(qry,(bookid, authid))
else:
    qry="insert into BOOK_author (bookid,authorid) values(?,?);"
    qry1="insert into author(firstname,lastname) values(?,?);"
    cur.execute(qry1,(firstname, lastname))
    cur1.execute(qry,(bookid, cur.lastrowid))

db.commit()


qry="insert into BOOK (name, description) values(?,?);"

db.close()
