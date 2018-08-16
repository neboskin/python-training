from tkinter import *
import backend

window=Tk()
window.wm_title("BOOKSTORE")


def view_command():
    lbox1.delete(0,END)
    for row in backend.view_db():
        lbox1.insert(END,row)


def search_command():
    lbox1.delete(0, END)
    for row in backend.search(author_val.get(),name_val.get(),ibn_val.get(),year_val.get()):
        lbox1.insert(END,row)


def add_command():
    backend.insert(author_val.get(),name_val.get(),ibn_val.get(),year_val.get())
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    view_command()


def get_selected_row(event):
    global sel_row
    try:
        index=lbox1.curselection()[0]
        sel_row = lbox1.get(index)
    except:
        pass



def command_delete():
    backend.delete(sel_row[0])
    view_command()


def command_update():
    backend.update(author_val.get(),name_val.get(),ibn_val.get(),year_val.get(),sel_row[0])
    view_command()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

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
e2=Entry(window,textvariable=name_val)
e2.grid(row=1,column=1)

ibn_val=StringVar()
e3=Entry(window,textvariable=ibn_val)
e3.grid(row=0,column=3)

year_val=StringVar()
e4=Entry(window,textvariable=year_val)
e4.grid(row=1,column=3)

lbox1=Listbox(window,height=6,width=35)
lbox1.grid(row=2,column=0,columnspan=2,rowspan=4)
scrl1=Scrollbar(window)
scrl1.grid(row=2,column=2,rowspan=4)

lbox1.configure(yscrollcommand=scrl1.set)
scrl1.configure(command=lbox1.yview())
lbox1.bind('<<ListboxSelect>>', get_selected_row)

btn1=Button(window, text='ViewAll',width=10,command=view_command)
btn1.grid(row=2,column=3)

btn2=Button(window, text='Find',width=10,command=search_command)
btn2.grid(row=3,column=3)

btn3=Button(window, text='Add',width=10,command=add_command)
btn3.grid(row=4,column=3)

btn4=Button(window, text='Update',width=10,command=command_update)
btn4.grid(row=5,column=3)

btn5=Button(window, text='Delete',width=10,command=command_delete)
btn5.grid(row=6,column=3)

btn6=Button(window, text='Close',width=10,command=window.destroy)
btn6.grid(row=7,column=3)

window.mainloop()


