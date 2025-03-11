import mysql.connector
a = mysql.connector.connect(host="localhost", port="3306", user = "root", password="1234", database = "python_db")
b =a.cursor()
def create():
    a = "Create table if not exists tb(id int Auto_increment primary key , name varchar(2500) not null, price int not null)"
    b.execute(a)
def add(x):
    y= x
    for i in range (y):
        y1=int(input("Enter the ID"))
        y2=input("Enter the name")
        y3=int(input("Enter the rate"))
        y4= (y1,y2,y3)
        y5 ="INSERT  INTO tb (id, name, price)VALUES (%s,%s,%s)"
        y6= (y4)
        b.execute(y5,y6)
        a.commit()
        print(b.rowcount,"Inserted")
def view():
    k ="Select * from  tb "
    b.execute(k)
    c = b.fetchall()
    for i in c:
        print(i)
def rem():
    t = int(input("Enter the id to be removed :"))
    t1 =b.execute("Delete from tb where id = '%s' ", t)
    
    
    
    a.commit()
    print(b.rowcount, "record(s) deleted")

print("1.Add a task")
print("2.view all task")
print("3.Remove a task")
print("4.Complete a task")
n = int(input("Enter the option : "))

create()
if n ==1:
    x=int(input("Enter the no row to be insert:"))

    add(x)
elif n == 2:
    view()
elif n == 3:
    rem()