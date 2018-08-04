nm=int(input())
lst=[int(x) for x in input().split()]
k=[]
for i in range(0,nm):
    for j in range(i+1,nm):
        if lst[i]==lst[j]:
            if lst[i] in k:
                k.remove(lst[i])
            else:k.append(lst[i])

for i in range(0,len(k)):
    if i<len(k)-1:
        d=' '
    else:d=''
    print(k[i],end=d)
