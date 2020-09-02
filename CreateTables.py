import sqlite3
db=sqlite3.connect('library.db')
try:
    cur =db.cursor()
    cur.execute('''CREATE TABLE BOOK (
    BookID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT (120) NOT NULL,
    Description TEXT (300));''')


    cur.execute('''CREATE TABLE AUTHOR (
    AuthorID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT (50) NOT NULL,
    LastName TEXT (50));''')

    cur.execute('''CREATE TABLE BOOK_AUTHOR (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    BookID INTEGER NOT NULL ,
    AuthorID INTEGER NOT NULL,
    
    CONSTRAINT fk_Book
    FOREIGN KEY (BookID)
    REFERENCES Book(Book_id),
    
    CONSTRAINT fk_Author
    FOREIGN KEY (AuthorID)
    REFERENCES Author(Author_id)
    );''')
except:
    print ('error in operation')
    db.rollback()
db.close()