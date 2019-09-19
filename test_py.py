'''
x=[1,2,3]
y=x
x=x.append(12)
print("x = ", x)
print("y = ", y)
'''
"""

n = "manish"

def capt(n):
    k = ""
    for i in range(len(n)):
        k + = n[i].upper() if i % 2 == 0 else n[i].lower()
    yield k
for i in capt(n):
    print (i)

"""
n ="Anish"
v=""
c=""
for i in range(len(n)):
    if (i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e'or i=='i' or i=='o'or i=='u'):
        v+= n[i]
    else:
        c+= n[i]
    
print(v)

print(c)
