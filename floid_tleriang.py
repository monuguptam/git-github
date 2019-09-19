""" r =int(input("inter the number of rows: "))
num =1
for row in range(1,r+1):
    for col in range(1,row+1):
        print(num,end = " ")
        num+=1   
    print()
"""
# fibonachi
n = int(input("enter the number upto u want fibonachi: "))
a,b=0,1
# while b<=n:
for i in range(0,n):
    if b<=i:
      print(b,end=" ")
      a,b=b,a+b
