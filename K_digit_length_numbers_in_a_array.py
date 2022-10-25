n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if i<0:
        i=i*(-1)
    d=0
    if i==0:
        d=1
    while i!=0:
        r=i%10
        i=i//10
        d+=1
    if d==k:
        c+=1
print(c)