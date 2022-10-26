n=int(input())
l=list(map(int,input().split()))
d=0
for i in l:
    l=0
    while i!=0:
        r=i%10
        i=i//10
        l+=r
    d+=l
print(d)