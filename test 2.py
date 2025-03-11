'''def func():
    yield 1
    yield 2
    yield 3
for values in func(): 
    print(values)'''
'''def func(limit):
    a,b = 0,1
    while a<limit:
        a,b = b , a+b 
        yield a 
x = func(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))'''
'''ls =[i for i in range (20)]
print(ls)'''
'''ls=[ i for i in range(20) if i%2 ==0]

x = max(ls)
print(ls)
print(x)'''
ls={ f"{i}*2={i*2}" for i in range (20)}
print(ls)

    
        


    
