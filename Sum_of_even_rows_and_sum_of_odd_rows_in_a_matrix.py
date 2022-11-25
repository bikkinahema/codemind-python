n,m=map(int,input().split())
l=[]
for i in range(n):
    p=list(map(int,input().split()))
    l.append(p)
c=0
d=0
for i in range(len(l)):
    if i%2==0:
        c+=sum(l[i])
    else:
        d+=sum(l[i])
print(c,d,end=" ")