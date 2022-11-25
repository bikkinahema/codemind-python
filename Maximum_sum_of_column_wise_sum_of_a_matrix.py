n,m=map(int,input().split())
l=[]
for i in range(n):
    p=list(map(int,input().split()))
    l.append(p)
a=[]
for i in range(m):
    c=0
    for j in range(n):
        c+=l[j][i]
    a.append(c)
print(max(a))
        