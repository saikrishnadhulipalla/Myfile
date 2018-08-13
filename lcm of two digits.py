n,m=map(int,input().split())
if n>m:
    sm=n
else:sm=m
while sm>0:
    if(sm%n==0) and (sm%m==0):
        c=sm
        break
    sm+=1
print(c)
