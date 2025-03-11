'''class banking():
    def create(self):
        list = ['enter the first name:', 'enter the last name:','enter the Acount no:',] 
        
        print("PLEASE ENTER YOUR DETAILS \n ---------------------------------------------------")
        for i  in list:
            print(i)
            if  i == 'enter the first name:':
                n = input()
            if  i == 'enter the last name:':
                y= input()
            if  i == 'enter the Acount no:':
                z= input()
        print("YOUR ACCOUNT DETAILS\n-------------------------------\n first name:",n,"\n last name:",  y , "\n Acount no:", z, "\n CHOOSE THE OPTION\n------------------------\n")
    def option (self, z):
        
        kk = ['check balance ', 'Deposit', 'withdraw']
        for  o,j  in enumerate (kk):
            print(o+1,j)
        for tt in range (10):
            r = int (input("enter your option :"))
            if r == 1 or 2 or 3 :
                
                if r != 1 :
                    w = int(input("enter amount: "))
                    if  r ==2:
                        print("Minimum balance", z)
                        z =z+w
                        print("Deposited amount:", z)
                    elif r ==3:
                        print("Minimum balance", z)
                        z =z-w
                        print("withdraw amount:", z)
                    
                    else:
                        print("Not have sufficient amount")
                else:
                    print("Minimum balance", z)

                
      

obj = banking()
obj.create()
k = 5000
print(obj.option(k))'''

class  kk:
    def __init__(Self):
        Self.a = 10
        Self.b= 20

class rr(kk):
    kk.__init__(Self)
    
    def __init__(Self):
        # kk.__init__(Self)
        Self.c = Self.a +  Self.b
    
    def jj(Self)
        
obj =rr()
obj1 = kk()
print(obj.c)




             
            