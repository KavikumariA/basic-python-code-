
import mysql.connector
c=mysql.connector.connect(host="localhost", port="3306", user = "root", password="1234", database = "python_db")
c1 = c.cursor()
class db():
    def main(Self):
        
        v = "Create table IF NOT EXISTS  ff(no int , product varchar(1000),  Quantity int, rate int) where not exist "
        c1.execute(v)
class db1(db):
    def bb(Self):
        db.main(Self )
        global d4
        for i in range (5):
            d =int(input("enter the no:"))
            d1 =input("enter the name:")
            d2 = int(input("enter the Quantity:"))
            d3= int(input("enter the rate:"))
            d4 = (d,d1,d2,d3)
            x ="Insert into ff1(no,product, Quantity, rate ) values(%s,%s,%s,%s)"
            y = (d4) 
            c1.executemany(x,y)
            c.commit()
            print(c1.rowcount," was inserted")
        
     

obj = db1()
obj.bb()
'''s ="Select product, Quantity *rate As total from var5"
c1.execute(s)
c.commit()'''





x1 ="Select * from ff"
c1.execute(x1)
d5=c1.fetchall()
for  j in d5:
    print(j)








