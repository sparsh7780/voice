#from re import U
import select
from tkinter import *
from turtle import onclick, onrelease
import customtkinter as ct
from PIL import ImageTk,Image
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox as mb

# username=StringVar()
# password=StringVar()

def connectdb(hostname,username,password):
    conn=None
    conn = mysql.connector.connect(
        host=hostname,
        user=username,
        passwd=password    
        )
    #print("Database connected succesfully")
    return conn
    

    
def q_exe(conn,query):
    cur1=conn.cursor()
    cur1.execute(query)
    
def fetch_d(conn,query):
    try:
        cur1=conn.cursor()
        cur1.execute(query)
        result=cur1.fetchall()
        return result
        #print(result)
    except Error as f:
        print(f"Error : {f}")
        
def insert_db(conn,query):
    cur1=conn.cursor()
    cur1.execute(query)
                
# conn = connectdb("localhost", "root","sparsh7780")
# db=input("enter database name")
# q1=(f"use {db}")    

def sign_in():
    username=e1.get()
    password=e2.get()
    unm=str(username)
    pwd=str(password)
    conn = connectdb("localhost", "root","sparsh7780")
    q_exe(conn,"use intern_sql")
    q3=("""Select username,password from user;""")
    val=fetch_d(conn,q3) #fetching username from table as a list(table is already created in sql)
    #print(val)
    flag=0
    #checking if username already exist
    for i in range(len(val)):
        if username==val[i][0] and password==val[i][1]:
            flag=1
    if flag==1:
        resp=mb.showinfo("Login Info",f"User {username.title()} has been login ")
    else:
        resp=mb.showwarning("Abort","Invalid Credentials")

        
def sign_up():
    username=e11.get()
    password=e21.get()
    unm=str(username)
    pwd=str(password)
    conn = connectdb("localhost", "root","sparsh7780")
    q_exe(conn,"use intern_sql")
    q3=("""Select username,password from user;""")
    val=fetch_d(conn,q3) 
#     tb=input("table to be used")   
#     val1=input("enter username value ")
#     val2=input("enter password value ")
#     q3=(f"insert into {tb} (username,password) values ( '{val1}','{val2}');")
#     insert_db(conn,q3) 
    #print(val)
    flag=0
    #checking if username already exist
    for i in range(len(val)):
        if username==val[i][0] and password==val[i][1]:
            flag=1
    if flag==1:
          resp=mb.showwarning("Abort","User already exist")
    else:
        q2=(f"Insert into user (username,password) values ('{unm}','{pwd}');")
        insert_db(conn,q2)
        conn.commit()
        resp=mb.showinfo("Login Info",f"Sign UP Succesfull")

        
def key_pressed(event):
    sign_in()
        
# root.bind("<Enter>",entry)
    

# root.title("sign in page")
# root.geometry("400x500")

# root.configure(bg="#000000")

# l1=Label(root,text="Username : ",font=("Times",20,"bold"))
# l1.place(x=150,y=100)

# l2=Label(root,text="Password : ",font=("Times",20,"bold"))
# l2.place(x=150,y=150)

# e1=Entry(root,font=("Times",20,"bold"))
# e1.place(x=300,y=100)

# e2=Entry(root,font=("Times",20,"bold"))
# e2.place(x=300,y=150)

# sign_b = Button(root,text="SIGN IN",font=("Times",16,"bold"),cursor="hand2",fg="blue",command=sign_in)
# sign_b.place(x=270,y=200)
# f2=Frame(f3,bg="white",width="430",height="590")
# f2.place(x=700,y=35)


# f3=Frame(root)
# f3.pack()

# def sign_up_p():
#     f2.destroy()
    
def sign_up_p():
    f2.destroy()
    
    a=Tk()

    f11=Frame(a)
    f11.pack(fill=X,side=TOP)

    l11=Label(f11,text="Welcome",bg="black",fg="white")
    l11.pack(fill=X)

    f31=Frame(a)
    f31.pack()

    p11=Image.open(r"C:\Users\ASUS\Downloads\img.png")
    #p2=p1.resize((500,500))
    p11=ImageTk.PhotoImage(p11)

    l21=Label(f31,image=p11)
    l21.pack()


    f21=Frame(f31,bg="white",width="430",height="590")
    f21.place(x=700,y=35)

    label=Label(f21,text="Welcome back",bg="white",fg="black",font="arial 20 bold").place(x=70,y=182)
    Label(f21,text="Please enter your details",bg="white",fg="grey",font="arial 8").place(x=74,y=220)

    global e11
    e11 = ct.CTkEntry(master=f21,
                                   placeholder_text="Username",
                                   width=200,
                                   height=40,
                                   border_width=2,
                                   bg_color="white",
                                   fg_color="white",
                                   text_color="black",
                                   textvariable="uservalue"
                                   )
    e11.place(relx=0.39, rely=0.5, anchor=CENTER)



    global e21
    e21 = ct.CTkEntry(master=f21,
                                   placeholder_text="Password",
                                   width=200,
                                   height=40,
                                   border_width=2,
                                   bg_color="white",
                                   fg_color="white",
                                   text_color="black",
                                   textvariable="passvalue"
                                   )
    e21.place(relx=0.39, rely=0.6, anchor=CENTER)

    button1 = ct.CTkButton(master=f21,
                                     width=200,
                                     height=32,
                                     border_width=0,
                                     corner_radius=8,
                                     text="Sign In",
                                     fg_color="#4e2a80",
                                     bg_color="#fff",
                                     text_color="#fff",
                                     hover_color="#503675",
                                     command=sign_in)
    button1.place(relx=0.39, rely=0.7, anchor=CENTER)

    a.bind("<Return>",key_pressed)
    #root.bind("<Up>",key_pressU)
    #root.bind("<Right>",key_pressr)


#     lab11=Label(f21,text="don't have an account? ",bg="white",fg="grey",font="arial 8")
#     lab11.place(x=74,y=800)

    
    a.mainloop()
    
    
    
    
    
def sign_in_p():

    root=Tk()
    
    root.title("SIGN IN PAGE")
    #root.geometry("400x500")
    
    f1=Frame(root)
    f1.pack(fill=X,side=TOP)

    l1=Label(f1,text="Welcome",bg="black",fg="white")
    l1.pack(fill=X)

    global f3
    f3=Frame(root)
    f3.pack()

    p1=Image.open(r"C:\Users\ASUS\Downloads\img.png")
    #p2=p1.resize((500,500))
    p1=ImageTk.PhotoImage(p1)

    l2=Label(f3,image=p1)
    l2.pack()

    global f2
    f2=Frame(f3,bg="white",width="430",height="590")
    f2.place(x=700,y=35)

    label=Label(f2,text="Welcome back",bg="white",fg="black",font="arial 20 bold").place(x=70,y=182)
    Label(f2,text="Please enter your details",bg="white",fg="grey",font="arial 8").place(x=74,y=220)

    global e1
    e1 = ct.CTkEntry(master=f2,
                                   placeholder_text="Username",
                                   width=200,
                                   height=40,
                                   border_width=2,
                                   bg_color="white",
                                   fg_color="white",
                                   text_color="black",
                                   textvariable="uservalue"
                                   )
    e1.place(relx=0.39, rely=0.5, anchor=CENTER)



    global e2
    e2 = ct.CTkEntry(master=f2,
                                   placeholder_text="Password",
                                   width=200,
                                   height=40,
                                   border_width=2,
                                   bg_color="white",
                                   fg_color="white",
                                   text_color="black",
                                   textvariable="passvalue"
                                   )
    e2.place(relx=0.39, rely=0.6, anchor=CENTER)

    button = ct.CTkButton(master=f2,
                                     width=200,
                                     height=32,
                                     border_width=0,cursor='hand2',corner_radius=8,
                                     text="Sign In",
                                     fg_color="#4e2a80",
                                     bg_color="#fff",
                                     text_color="#fff",
                                     hover_color="#503675",
                                     command=sign_in)
    button.place(relx=0.39, rely=0.7, anchor=CENTER)

    root.bind("<Return>",key_pressed)
    #root.bind("<Up>",key_pressU)
    #root.bind("<Right>",key_pressr)


    lab1=Label(f2,text="Don't have an account? ",bg="white",fg="black",font="arial 8")
    lab1.place(relx=0.32, rely=0.8, anchor=CENTER)

    button2 = ct.CTkButton(master=f2,
                                     width=40,
                                     height=32,
                                     border_width=0,cursor='hand2',corner_radius=2,
                                     text="Sign Up",
                                     bg_color="white",
                                     fg_color="#fff",
                                     text_color="blue",
                                     hover_color="#fff",
                                     command=sign_up_p)
    button2.place(relx=0.51, rely=0.8, anchor=CENTER)
    
    root.mainloop()
sign_in_p()

