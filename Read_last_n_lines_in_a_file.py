f=open('sample.txt','r')
n=int(input())
str=f.readlines()
for i in range (1,n+1):
    print(str[-i])
f.close()
