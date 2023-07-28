#pip install mysql.connector
import mysql.connector


def connectdb(hostname,username,password):
    conn=None
    conn = mysql.connector.connect(
        host=hostname,
        user=username,
        passwd=password    
        )
    return conn
    print("Database connected succesfully")
    
    
def q_exe(conn,query):
    cur1=conn.cursor()
    cur1.execute(query)


conn = connectdb("localhost", "root","sparsh7780")
db=input("enter database name")
q1=(f"use {db}")
q_exe(conn,q1)

# def entry():
#     username=e1.get()
#     password=e2.get()
#     unm=str(username)# converting stringvar() to string 
#     psw=str(password)
#     conn=connectdb("localhost","root","Siddh@1310") #connecting to database(database is already created in sql)
#     q_exe(conn,"use admn;")#use databasename
#     q3=("""Select user_name from cred;""") #query for displaying only username from table
    # val=(fetch(conn,q3))#fetching username from table as a list(table is already created in sql)
    # flag=0
    # #checking if username already exist
    # for i in range(len(val)):
    #     if username==val[i][0]:
    #         flag=1
    # if flag==1:
    #       resp=mb.showwarning("Abort","User already exist")
    # else:
    #     q2=(f"Insert into cred (user_name,user_password) values ('{unm}','{psw}');")
    #     q_insert(conn,q2)
    #     resp=mb.showinfo("Login Info",f"Sign UP Succesfull")



# def gui():
#     a=Tk()

#     a.title("gui")