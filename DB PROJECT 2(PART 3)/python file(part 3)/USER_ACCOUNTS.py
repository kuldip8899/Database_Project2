import tkinter as tk
from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(host="acadmysqldb001p", user="kxs2000", passwd = "Kd8490001906#", database = "kxs2000", auth_plugin= "mysql_native_password")
cursor = mydb.cursor()

def add():
    c1 = e1.get()
    c2 = e2.get()
    c3 = e3.get()
    c4 = e4.get()

    sql = "INSERT INTO USER_ACCOUNTS VALUES(%s, %s, %s, %s)"
    cursor.execute(sql, (c1,c2,c3,c4))
    print("USER_ACCOUNTS recorD inserted")
    mydb.commit()
    return True

win = Tk()

frm1 = Frame(win)
frm1.pack(side=tk.LEFT, padx=20)




v1 = StringVar()
c1 = StringVar()

l1 = Label(frm1,fg='blue',bg='yellow',relief="solid",font = ("Arial" , 14), textvariable = v1, text = "USER_ID_NO")
v1.set("USER_ID_NO")
l1.grid(row=1, column=1)

e1 = Entry(frm1, textvariable=c1)
e1.grid(row=1, column=2)


v2 = StringVar()
c2 = StringVar()

l2 = Label(frm1,fg='red',bg='white',relief="solid", font = ("Arial" , 14), textvariable = v2, text = "USER_NAME")
v2.set("USER_NAME")
l2.grid(row=2, column=1)

e2 = Entry(frm1, textvariable=c2)
e2.grid(row=2, column=2)


v3 = StringVar()
c3 = StringVar()

l3 = Label(frm1,fg='black', bg='blue',relief="solid",font = ("Arial" , 14), textvariable = v3, text = "USER_PHONE_NO")
v3.set("USER_PHONE_NO")
l3.grid(row=3, column=1)

e3 = Entry(frm1, textvariable=c3)
e3.grid(row=3, column=2)


v4 = StringVar()
c4 = StringVar()

l4 = Label(frm1,fg='white', bg='red',relief="solid",font = ("Arial" , 14), textvariable = v4, text = "USER_ROLES")
v4.set("USER_ROLES")
l4.grid(row=4, column=1)

e4 = Entry(frm1, textvariable=c4)
e4.grid(row=4, column=2)



btn = Button(frm1, text="USER_ACCOUNTS RECORD", command = add)
btn.grid(row=5, column=2)

win.title("USER_ACCOUNTS")
win.geometry("300x300")
win.mainloop()