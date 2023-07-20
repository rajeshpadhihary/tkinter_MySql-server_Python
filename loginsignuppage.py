from tkinter import *
import mysql.connector as connector

connectionObj = connector.connect(host = "localhost",user = "rajesh",database = "rajesh",passwd = "Rajesh@1588")
cursorObj = connectionObj.cursor()
regN = "SELECT COUNT(regNo) FROM students;"
cursorObj.execute(regN)
x=cursorObj.fetchall()
for item in x:
    print(f"At the time of SignUp,\n\tYour regNo must be greater than {item[0]}")

def SignUp():
    window = Tk()
    window.geometry("400x300")
    window.title("Student SignUp")
    regNo = Label(window,text="Reg no: ")
    regNo.grid(row=0,column=0)
    name = Label(window,text="Name: ")
    name.grid(row=1,column=0)
    mark = Label(window,text="Mark: ")
    mark.grid(row=2, column=0)
    passwd = Label(window,text="Password: ")
    passwd.grid(row=3,column=0)
    regData = Entry(window)
    regData.grid(row=0,column=1)
    nameData = Entry(window)
    nameData.grid(row=1,column=1)
    markData = Entry(window)
    markData.grid(row=2,column=1)
    passwordData = Entry(window,show='*') # show password with asterisk(*)
    passwordData.grid(row=3,column=1)
    data = Label(window,text="NOTE: Be carefull when you insert your data")
    data.grid(row=5,column=1)
    def fun():
        connectionObj = connector.connect(host = "localhost",user = "rajesh",database = "rajesh",passwd = "Rajesh@1588")
        cursorObj = connectionObj.cursor()
        regNo = regData.get()
        name = nameData.get()
        mark = markData.get()
        password = passwordData.get()
        sqlQuery = f"INSERT INTO students (regNo,name,mark,password) values ({regNo},'{name}',{mark},'{password}')"
        cursorObj.execute(sqlQuery)
        connectionObj.commit()
        print("Successfully Signed Up..... CONGRATS...")
    Button(window,text="SUBMIT",borderwidth=3,bg="grey",relief=SUNKEN,padx=20,command=fun).grid(row=4,column=1)
    Button(window,text="EXIT",borderwidth=3,bg="grey",relief=SUNKEN,padx=20,command=window.destroy).grid(row=4,column=2)
    window.mainloop()

def LogIn():
    window = Tk()
    window.geometry("400x300")
    window.title("Student Login")
    regNo = Label(window,text="Reg no: ")
    regNo.grid(row=0,column=0)
    passwd = Label(window,text="Password: ")
    passwd.grid(row=1,column=0)
    regData = Entry(window)
    regData.grid(row=0,column=1)
    passData = Entry(window,show="*")
    passData.grid(row=1,column=1)
    data = Label(window,text="NOTE: ENTER DATA CAREFULLY.")
    data.grid(row=3,column=1)
    def fun():
        connectionObj = connector.connect(host = "localhost",user = "rajesh",database = "rajesh",passwd = "Rajesh@1588")
        cursorObj = connectionObj.cursor()
        regNo = regData.get()
        password = passData.get()
        sqlQuery = f"SELECT * FROM students WHERE regNo = {regNo} AND password = '{password}'"
        cursorObj.execute(sqlQuery)
        result = cursorObj.fetchall()
        if len(result) == 0:
            print("Invalid Username or Password")
        for record in result:
            print(f"Hey {record[1]},\n\tYou are successfully loged in.Your data is in below.")
            print ("Reg No --->",record[0])
            print ("Name --->",record[1])
            print ("Mark --->",record[2])
            print ("Password --->",record[3])
    Button(window,text="SUBMIT",borderwidth=3,bg="grey",relief=SUNKEN,padx=20,command=fun).grid(row=2,column=1)
    Button(window,text="EXIT",borderwidth=3,bg="grey",relief=SUNKEN,padx=20,command=window.destroy).grid(row=2,column=3)
    window.mainloop()
print('''
        Enter 1 for SignUp
        Enter 2 for Login
	''')
choice = int(input("Enter your choice: "))
if choice == 1:
    SignUp()
elif choice == 2:
    LogIn()
else:
    print('Wrong Choice!!! Try Again.')