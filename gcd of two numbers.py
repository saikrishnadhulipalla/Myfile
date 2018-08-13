n,m=map(int,input().split())
if n>m:
    sm=n
else:sm=m
for i in range(1,sm+1):
    if(n%i==0) and (m%i==0):
        c=i
print(c)
