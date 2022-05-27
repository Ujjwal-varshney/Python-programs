n=int(input("enter the number:"))
c=0
if(n==2):
    print("prime number")
else:
    for i in range(1,n//2+1):
        if(n%i==0):
            c+=1
    if(c==1):
        print("prime number")
    else:
        print("not prime number")
