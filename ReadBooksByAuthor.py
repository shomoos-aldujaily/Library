import sqlite3
db=sqlite3.connect('library.db')
sql="SELECT b.* from book b inner join book_author m on b.bookid = m.bookid inner join author a on a.authorid = m.authorid where upper(a.firstname)=upper(?) and upper(lastname)=upper(?);"
first=input('Enter author first name')
last=input('Enter author last name')
cur=db.cursor()
cur.execute(sql,(first,last))
while True:
    record=cur.fetchone()
    if record==None:
        break
    print (record)
db.close()
