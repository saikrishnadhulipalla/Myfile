nm=input()
evn=""
odd=""
for i in range(0,len(nm)):
    if (i)%2==0:
        evn=evn+(nm[i])
    else:
        odd=odd+(nm[i])
print(evn,odd)
