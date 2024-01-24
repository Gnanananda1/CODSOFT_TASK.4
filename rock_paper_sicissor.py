f=True
while(f):
    import random
    a=int(input("enter 1 for rock,2 for paper,3 for scissors"))
    if(a==1):
        b="rock"
    elif(a==2):
        b="paper"
    elif(a==3):
        b="scissors"
    else:
        print("enter valid input")
        break
    l=["rock","paper","scissors"]
    c=random.choice(l)
    print("user choice:",b)
    print("computer choice:",c)
    if(b==c):
        print("it's a tie")
    elif(b=="rock" and c=="scissors"):
        print("user wins")
    elif(b=="scissors" and c=="paper"):
        print("user wins")
    elif(b=="paper" and c=="rock"):
        print("user wins")
    else:
       print("user loses")
    v=int(input("if you want to play again enter 1 or enter any number"))
    if(v==1):
        f=True
    else:
        f=False
       
        

    
    
