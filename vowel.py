'''
s =input("Enter the string : ")
#ls =list(s)
#v=[]
#c=[]
vo=""
co=""
for i in s:
    if (i=="A" or i=="E" or i=="O" or i=="U" or i=="I" or i=="a" or i=="e" or i=="o" or i=="u" or i=="i"):
        #v.append(i)
        vo += i
    else:
        #c.append(i)
        co += i

#rint(vo.join(v))
#print(co.join(c))
print(vo)
print(co)

'''
string =input("enter the string to be reversed : ")

rev=""
for i in string:
    rev=i+rev
print(rev)
