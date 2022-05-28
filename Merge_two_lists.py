def merge(*lst):
    lst=[]
    for i in lst1:
        lst.append(i)
    for i in lst2:
        lst.append(i)
    print(lst)
lst1=[]
lst2=[]
lst1=list(map(eval,input().split()))
lst2=list(map(eval,input().split()))
merge(lst1,lst2)
