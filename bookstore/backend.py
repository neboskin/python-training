import sqlite3


def create_table():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute("create table if not exists books (ID INTEGER PRIMARY KEY, author TEXT, name TEXT, ibnn TEXT, year INTEGER)")
    conn.commit()
    conn.close()


def insert(a,n,i,y):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute("insert into books values(Null,?,?,?,?)",(a,n,i,y))
    conn.commit()
    conn.close()


def view_db():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from books")
    res=cur.fetchall()
    conn.close()
    return res


def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("delete from books where id=?",(id,))
    conn.commit()
    conn.close()


def search(a='',n='',i='',y=''):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    res=cur.execute("select * from books where author=? OR name=? OR ibnn=? OR year=?", (a,n,i,y))
    res=res.fetchall()
    conn.close()
    return res


def update(a,n,i,y,id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("update books set author=?, name=?, ibnn=?, year=? where id=?", (a, n, i, y,id))
    conn.commit()
    conn.close()


create_table()
