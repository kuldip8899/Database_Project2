import tkinter as tk
from tkinter import *
import mysql.connector
mydb = mysql.connector.connect(host="acadmysqldb001p", user="kxs2000", passwd = "Kd8490001906#", database = "kxs2000", auth_plugin= "mysql_native_password")
cursor = mydb.cursor()

def add():
    c1 = e1.get()
    c2 = e2.get()
    c3 = e3.get()
    

    sql = "INSERT INTO USER_ROLES VALUES(%s, %s, %s)"
    cursor.execute(sql, (c1,c2,c3))
    print("USER_ROLES record added")
    mydb.commit()
    return True

win = Tk()

frm1 = Frame(win)
frm1.pack(side=tk.LEFT, padx=20)




v1 = StringVar()
c1 = StringVar()

l1 = Label(frm1,fg='blue',bg='yellow',relief="solid",font = ("Arial" , 14), textvariable = v1, text = "ROLE_ID")
v1.set("ROLE_ID")
l1.grid(row=1, column=1)

e1 = Entry(frm1, textvariable=c1)
e1.grid(row=1, column=2)

v2 = StringVar()
c2 = StringVar()

l2 = Label(frm1, fg='red',bg='white',relief="solid", font = ("Arial" , 14), textvariable = v2, text = "ROLE_NAME")
v2.set("ROLE_NAME")
l2.grid(row=2, column=1)

e2 = Entry(frm1, textvariable=c2)
e2.grid(row=2, column=2)

v3 = StringVar()
c3 = StringVar()

l3 = Label(frm1,fg='black', bg='blue',relief="solid",font = ("Arial" , 14), textvariable = v3, text = "DESCRIPTION")
v3.set("DESCRIPTION")
l3.grid(row=3, column=1)

e3 = Entry(frm1, textvariable=c3)
e3.grid(row=3, column=2)



btn = Button(frm1, text="USER_ROLES RECORD", command = add)
btn.grid(row=5, column=2)

win.title("USER_ROLES")
win.geometry("300x300")
win.mainloop()