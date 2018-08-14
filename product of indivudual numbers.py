nm=int(input())
pro=1
while nm>0:
    rem=nm%10
    pro=rem*pro
    nm=nm//10
print(pro)
