lw,up=input().split()
lw=int(lw)
up=int(up)
lst=[]
for nm in range(lw,up):
    temp=nm
    sum=0
    order=len(str(nm))
    while nm >0:
        dg=nm % 10
        sum+=dg**order
        nm=nm//10
    if(temp==sum):
        lst.append(temp)
for i in range(0,len(lst)):
    if i<len(lst)-1:
        k=' '
    else:k=''
    print(lst[i],end=k)
