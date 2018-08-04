nm=int(input())
lst=[int(x) for x in input().split()]
k=[]
for i in range(0,nm):
    if i==lst[i]:
        k.append(lst[i])
for i in range(0,len(k)):
    if i<len(k)-1:
        d=' '
    else:d=''
    print(k[i],end=d)
if k==[]:
    print("'-1'")
