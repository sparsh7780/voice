root=Tk()

# def connectdb(hostname,username,password):
#     conn=None
#     conn = mysql.connector.connect(
#         host=hostname,
#         user=username,
#         passwd=password    
#         )
#     print("Database connected succesfully")
#     return conn
    

    
# def q_exe(conn,query):
#     cur1=conn.cursor()
#     cur1.execute(query)
    
# def fetch_d(conn,query):
#     try:
#         cur1=conn.cursor()
#         cur1.execute(query)
#         result=cur1.fetchall()
#         return result
#         #print(result)
#     except Error as f:
#         print(f"Error : {f}")
        
# def insert_db(conn,query):
#     cur1=conn.cursor()
#     cur1.execute(query)
                
# # conn = connectdb("localhost", "root","sparsh7780")
# # db=input("enter database name")
# # q1=(f"use {db}")    

# def sign_in():
#     username=e1.get()
#     password=e2.get()
#     unm=str(username)
#     pwd=str(password)
#     conn = connectdb("localhost", "root","sparsh7780")
#     q_exe(conn,"use intern_sql")
#     q3=("""Select username,password from user;""")
#     val=fetch_d(conn,q3) #fetching username from table as a list(table is already created in sql)
#     #print(val)
#     flag=0
#     #checking if username already exist
#     for i in range(len(val)):
#         if username==val[i][0] and password==val[i][1]:
#             flag=1
#     if flag==1:
#         resp=mb.showinfo("Login Info",f"User {username.title()} has been login ")
#     else:
#         resp=mb.showwarning("Abort","Invalid Credentials")

        
# def sign_up():
#     username=e1.get()
#     password=e2.get()
#     unm=str(username)
#     pwd=str(password)
#     conn = connectdb("localhost", "root","sparsh7780")
#     q_exe(conn,"use intern_sql")
#     q3=("""Select username,password from user;""")
#     val=fetch_d(conn,q3) 
# #     tb=input("table to be used")   
# #     val1=input("enter username value ")
# #     val2=input("enter password value ")
# #     q3=(f"insert into {tb} (username,password) values ( '{val1}','{val2}');")
# #     insert_db(conn,q3) 
#     #print(val)
#     flag=0
#     #checking if username already exist
#     for i in range(len(val)):
#         if username==val[i][0] and password==val[i][1]:
#             flag=1
#     if flag==1:
#           resp=mb.showwarning("Abort","User already exist")
#     else:
#         q2=(f"Insert into user (username,password) values ('{unm}','{pwd}');")
#         insert_db(conn,q2)
#         conn.commit()
#         resp=mb.showinfo("Login Info",f"Sign UP Succesfull")

        
# def key_pressed(event):
#     sign_in()
        
# # root.bind("<Enter>",entry)
    

# root.title("sign in page")
# root.geometry("400x500")



# #root.configure(bg="#000000")

# Label(root,text="Student Management system",font=("Times",24,"bold")).place(anchor=CENTER) 

# l1=Label(root,text="Username : ",font=("Times",20,"bold"))
# l1.place(x=150,y=300)

# l2=Label(root,text="Password : ",font=("Times",20,"bold"))
# l2.place(x=150,y=350)

# e1=Entry(root,font=("Times",20,"bold"))
# e1.place(x=300,y=300)

# e2=Entry(root,font=("Times",20,"bold"))
# e2.place(x=300,y=350)

# sign_b = Button(root,text="SIGN IN",font=("Times",16,"bold"),cursor="hand2",fg="blue",command=sign_in)
# sign_b.place(x=270,y=200)


# root.bind("<Return>",key_pressed)

    
    
# root.mainloop()
