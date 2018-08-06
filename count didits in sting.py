nm=input()
k=[]
for i in range(0,len(nm)):
    if (nm[i]>='a' and nm[i]<='z') or (nm[i]>='A' and nm[i]<='Z'):
        c=0
    else:k.append(nm[i])
for j in range (0,len(k)):
    print(k[j],end='')
