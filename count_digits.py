n=int(input())
l=list(map(int,input().split()))
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
    print(d, end=' ')