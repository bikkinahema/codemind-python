n=int(input())
l=list(map(int,input().split()))
m=0
for i in l:
    s=str(i)
    if len(s)>m:
        m=len(s)
c=0
for i in l:
    k=str(i)
    if len(k)==m:
        c+=1
print(c)