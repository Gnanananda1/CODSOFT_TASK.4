import random
import string
import sys
p=""
n=int(input("enter the length of the password"))
a=int(input("enter  1 if you want any special characters in your password or enter any number"))
if(a==1):
    l1=["!","@","#","%","$","^","&","*","/","?","."]
    b=int(input("enter no of special characters in your password"))
    if(b>n):
        print("your pass word length is insuffcient")
        sys.exit()
    else:
        for j in range(b):
            k=random.choice(l1)
            p=p+k
else:
    b=0
c=int(input("enter 1 if you want to include numbers in your pass word"))
if(c==1):
    d=int(input("enter no of numbers in your password"))
    if(d+b>n):
        print("your pass word length is insuffcient")
        sys.exit()
    else:
        l2=["1","2","3","4","5","6","7","8","9","0"]
        for m in range(d):
            h=random.choice(l2)
            p=p+h
else:
    d=0
l=list(string.ascii_letters)
for i in range(n-(b+d)  ):
    c=random.choice(l)
    p=p+c
l5=list(p)
random.shuffle(l5)
r="".join(l5)
print(r)

