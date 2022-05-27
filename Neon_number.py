import math
n=int(input("enter the number:"))
m=n
s=math.pow(n,2)
sum=0
while(s>0):
    r=s%10
    sum=sum+r
    s=s//10
if(sum==m):
    print("neon number")
else:
    print("not a neon number")
