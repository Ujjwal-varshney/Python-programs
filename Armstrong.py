n=int(input("enter the number:"))
d=0
m=n
while(n>0):
    d+=1
    n=n//10
sum=0
l=m
while(m>0):
    h=m%10
    sum=sum+h**d
    m=m//10
if(l==sum):
    print("armstrong")
else:
    print("not armstrong")
