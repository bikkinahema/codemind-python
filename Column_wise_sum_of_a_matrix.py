n,m=map(int,input().split())
l=[]
for i in range(n):
    p=list(map(int,input().split()))
    l.append(p)
for i in range(m):
    c=0
    for j in range(n):
        c+=l[j][i]
    print(c,end=" ")