n = []
n3=[]
n4=[]
b= "Book"
b1=[]
h=[]
for i in range (3):
    
    n2 =int(input("Enter the  number1"))
    n6 =int(input("Enter the  number2"))
    b1.append(b)
    nh=[n2,n6]
    
    n3.append(nh)
    

                
                    
                
    
print(b1)
print(n3)
for i in n3:
        for j in i:
            h.append(j)
r = set()
s = set()
r1=[]

for number in h:
    if number in s:
        r1.append(number)
        r.add(number)
        print(r1)
        
        
    else:
        s.add(number)
        
        


