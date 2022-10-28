n=int(input())
l=list(map(int,input().split()))
p=min(l)
a=str(p)
m=len(a)
c=0
for i in l:
    k=str(i)
    if len(k)==m:
        c+=1
print(c)