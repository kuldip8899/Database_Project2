import tkinter as tk
from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(host="acadmysqldb001p", user="kxs2000", passwd = "Kd8490001906#", database = "kxs2000", auth_plugin= "mysql_native_password")
cursor = mydb.cursor()

def add():
    cname1 = ent1.get()
    if var2_1.get() == 1:
        cname2 = "Account"
    if var2_1.get() == 2:
        cname2 = "Relational"
    else :
        print("Privilege_Type can be only one value")
    cname3 = ent3.get()
    cname4 = ent4.get()

    sql: str = "INSERT INTO PRIVILEGES VALUES(%s, %s, %s, %s)"
    cursor.execute(sql, (cname1,cname2,cname3,cname4))
    if cname2 == "Account":
        print("account_PRIVILEGES record found")
        sql: str = "INSERT INTO OWNS VALUES(%s, %s)"
        cursor.execute(sql, (cname4, cname1))
        print("PRIVILEGES record added")
        mydb.commit()
    mydb.commit()
    if cname2 == "Relational":
        print("relational_PRIVILEGES record found")
        sql: str = "INSERT INTO BELONGSTO VALUES(%s, %s)"
        cursor.execute(sql, (cname4, cname1))
        print("PRIVILEGES record added")
        mydb.commit()
    mydb.commit()



    return True

win = Tk()

frm1 = Frame(win)
frm1.pack(side=tk.LEFT, padx=20)


var1 = StringVar()
cname1 = StringVar()

label1 = Label(frm1,fg='red',bg='white',relief="solid", font = ("Arial" , 14), textvariable = var1,text = "P_ID")
var1.set("P_ID")
label1.grid(row=1, column=1)

ent1 = Entry(frm1, textvariable=cname1)
ent1.grid(row=1, column=2)


var2 = StringVar()
cname2 = StringVar()

label2 = Label(frm1,fg='black', bg='blue',relief="solid",font = ("Arial" , 14), textvariable = var2, text = "P_TYPE")
var2.set("P_TYPE")
label2.grid(row=2, column=1)

var2_1 = IntVar()
r1 = Radiobutton(frm1, text="Account", variable=var2_1,value=1).grid(row=2, column=2)
r2 = Radiobutton(frm1, text="Relational", variable=var2_1,value=2).grid(row=2, column=3)




var3 = StringVar()
cname3 = StringVar()

label3 = Label(frm1,fg='white', bg='red',relief="solid",font = ("Arial" , 14), textvariable = var3, text = "DESCRIPTION")
var3.set("DESCRIPTION")
label3.grid(row=3, column=1)

ent3 = Entry(frm1, textvariable=cname3)
ent3.grid(row=3, column=2)

var4 = StringVar()
cname4 = StringVar()

label4 = Label(frm1,fg='orange', bg='black',relief="solid",font = ("Arial" , 14), textvariable = var4, text =  "PNAME")
var4.set("PNAME")
label4.grid(row=4, column=1)

ent4 = Entry(frm1, textvariable=cname4)
ent4.grid(row=4, column=2)


btn = Button(frm1, text="PRIVILEGES RECORD", command = add)
btn.grid(row=5, column=2)

win.title("PRIVILEGES")
win.geometry("350x300")
win.mainloop()