a,b,c=map(int,input().split())
s=0
for i in  range(1,a+1):
    s=s+(b+(i-1)*c)
print(s)
