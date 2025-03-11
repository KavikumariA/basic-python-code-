import mysql.connector
con = mysql.connector.connect(host="localhost", port="3306", user = "root", password="1234", database = "python_db")
'''cursor = con.cursor()
selectQry = "select * from Persons"
cursor.execute(selectQry)
record = cursor.fetchall()

print(cursor.rowcount)
for row in record:
    print(row[0])
    print(row[1])
    print(row[2])

cursor.close()
con.close()'''
print(con)
py = con.cursor()
v ="select * from Persons"
'''v1 ="DELETE FROM persons WHERE PersonID = %s "'''
py.execute(v)
for x in py:
    print(x)
    