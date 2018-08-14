from tkinter import *
import sqlite3
def create_table():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute("create table if not exists books ('Athor' TEXT, 'Name', TEXT, 'IBNN' TEXT, 'Year' INTEGER)")
    conn.commit()
    conn.close()


def insert(a,n,i,y):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute("insert into books values('%s','%s','%s','%s')"%(a,n,i,y))
    conn.commit()
    conn.close()


def init_interface():
    window=Tk()

    lb1=Label(window,text='Author')
    lb1.grid(row=0,column=0)

    lb2=Label(window,text='Name')
    lb2.grid(row=1,column=0)

    lb3=Label(window,text='IBNN')
    lb3.grid(row=0,column=2)

    lb4=Label(window,text='Year')
    lb4.grid(row=1,column=2)

    author_val=StringVar()
    e1=Entry(window,textvariable=author_val)
    e1.grid(row=0,column=1)

    name_val=StringVar()
    e1=Entry(window,textvariable=name_val)
    e1.grid(row=1,column=1)

    ibn_val=StringVar()
    e1=Entry(window,textvariable=ibn_val)
    e1.grid(row=0,column=3)

    year_val=StringVar()
    e1=Entry(window,textvariable=year_val)
    e1.grid(row=1,column=3)

    lbox1=Listbox(window,height=6,width=35)
    lbox1.grid(row=2,column=0,columnspan=2,rowspan=4)
    scrl1=Scrollbar(window)
    scrl1.grid(row=2,column=2,rowspan=4)

    lbox1.configure(yscrollcommand=scrl1.set)
    scrl1.configure(command=lbox1.yview())

    btn1=Button(window, text='ViewAll',width=10)
    btn1.grid(row=2,column=3)

    btn2=Button(window, text='Find',width=10)
    btn2.grid(row=3,column=3)

    btn3=Button(window, text='Add',width=10,command=insert(author_val.get(),name_val.get(),ibn_val.get(),year_val.get()))
    btn3.grid(row=4,column=3)

    btn4=Button(window, text='Update',width=10)
    btn4.grid(row=5,column=3)

    btn5=Button(window, text='Delete',width=10)
    btn5.grid(row=6,column=3)

    btn6=Button(window, text='Close',width=10)
    btn6.grid(row=7,column=3)

    window.mainloop()


init_interface()
create_table()


