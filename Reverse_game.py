n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    l=0
    while i!=0:
        r=i%10
        i=i//10
        l=l*10+r
    a.append(l)
print(*a)
    