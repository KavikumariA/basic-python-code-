ls1 = [range(0,100)]
from functools import reduce
ls = reduce(lambda x ,y: x+y , ls1)
print(ls)