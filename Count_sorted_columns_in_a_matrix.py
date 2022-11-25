n,m=map(int,input().split())
l=[]
for i in range(n):
    p=list(map(int,input().split()))
    l.append(p)
s=0
for i in range(m):
    c=[]
    for j in range(n):
        c.append(l[j][i])
    k=sorted(c)
    if (c==k)  or (k[::-1]==c):
        s+=1
print(s)