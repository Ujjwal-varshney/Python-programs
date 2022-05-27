n=int(input("eneter the number:"))
sum_odd=0
sum_even=0
while(n>0):
    rev=n%10
    sum_even=sum_even+rev
    n=n//10
    rod=n%10
    sum_odd=sum_odd+rod
    n=n//10
print("sum of even places",sum_even)
print("sum of odd places",sum_odd)
