n=int(input())
t=n
k=n
while n>0:
    t+=1
    p=t
    rev=0
    while p!=0:
        r=p%10
        p=p//10
        rev=rev*10+r
    if rev==t:
        ma=t
        break
while n>0:
    k-=1
    w=k
    rev1=0
    while w!=0:
        r1=w%10
        w=w//10
        rev1=rev1*10+r1
    if rev1==k:
        mi=k
        break
maxi=ma-n
mini=n-mi
if maxi<mini:
    print(ma)
elif mini<maxi:
    print(mi)
else:
    print(mi,ma,end=' ')
        