n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    t=i
    l=0
    while i!=0:
        r=i%10
        i=i//10
        l=l*10+r
    if l==t:
        c+=1
print(c)