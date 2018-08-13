nm=int(input())
rev=0
if nm<1000:
    while nm>0:
        rem=nm%10
        rev=(rev*10)+rem
        nm=nm//10
    print(rev)
