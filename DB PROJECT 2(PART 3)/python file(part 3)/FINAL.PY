import tkinter
window = tkinter.Tk()
window.title('PROJECT 2 GUI')

window_width = 500
window_height = 500

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def redirect1():
	import USER_ACCOUNTS 
def redirect2():
	import USER_ROLES 
def redirect3():
	import PRIVILEGES 
def redirect4():
	import TABLES 

b1 = tkinter.Button(window, text = "USER_ACCOUNTS" ,fg='blue',bg='yellow',relief="solid", font = ("Arial" , 14),command = redirect1)
b1.grid(row =0 ,column = 0 , sticky = tkinter.W)
b2 = tkinter.Button(window, text = "USER_ROLES" ,fg='red',bg='white',relief="solid", font = ("Arial" , 14),command = redirect2)
b2.grid(row =1 ,column = 0 , sticky = tkinter.W)
b3 = tkinter.Button(window, text = "PRIVILEGES" ,fg='black',bg='blue',relief="solid", font = ("Arial" , 14),command = redirect3)
b3.grid(row =3 ,column = 0 , sticky = tkinter.W)
b4 = tkinter.Button(window, text = "TABLES" ,fg='white',bg='red',relief="solid", font = ("Arial" , 14),command = redirect4 )
b4.grid(row =4 ,column = 0 , sticky = tkinter.W)
window.mainloop()