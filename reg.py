import re

n = input("Enter your email id:")
v = re.compile ='^.*(?=.*[a-z])(?=.*\d)(?=.*[@gmail\.com]).*$'
r = re.findall(v,n)

print(r)
if (r):
    print("valid email ID")
else:
    print("Invalid email ID")


