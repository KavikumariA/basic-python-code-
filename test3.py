'''def func(limit):
    a,b = 0,1
    while a<limit:
        yield a 
        a,b = b , a+b 
       
x = func(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))'''

'''
def double(n):
    return n*n
ls = (range(10))
ls3 = map(double,ls)
print(list(ls3))
'''
ls=["kavi","kumari"]
name=''
def kavi(a):
    global name 
    name +=a
   
map(kavi,ls)
print(name)
print(list(name))

    
    