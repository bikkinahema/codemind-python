n,m=map(int,input().split())
l=[]
for i in range(n):
    p=list(map(int,input().split()))
    l.append(p)
c=0
for i in l:
    k=sorted(i)
    if (i==k) or (k[::-1]==i):
        c+=1
print(c)