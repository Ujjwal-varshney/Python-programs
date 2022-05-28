num=int(input("enter the number:"))
i=1
sum=0
while(i<=num//2):
    if(num%i==0):
        sum=sum+i
    i+=1
if(num==sum):
    print("the number is perfect number!")
else:
    print("the number is not a perfect number!")
