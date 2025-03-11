from bs4 import BeautifulSoup
import requests
import csv
c1=[['TITLE', 'HEADING'],]

y  =['apple', 'kiwi','watermelon']
x1=int(input("enter the no of string: "))
for i in range(x1):
    x=input("enter the string: ")
    y.append(x)



for i in y:
    u = requests.get("https://en.wikipedia.org/wiki/"+i)
    con = BeautifulSoup(u.content, 'html.parser')
    v = con.find('div',class_="mw-heading mw-heading2").text
    v1= con.find('title').text
    print(v1)

    print(v)
    r=[v1,v]
    c1.append(r)
    
# for i in c1:
#     print(i)
with open('w1.csv',mode='w',newline='',encoding='utf-8') as file:
    write=csv.writer(file)
    for i in c1:
        write.writerow(i)
            


