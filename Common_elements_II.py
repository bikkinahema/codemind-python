n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
k=[]
for i in a:
    c=0
    for j in b:
        if j==i:
            c+=1
            pass
    if c==0:
        l.append(i)
for i in b:
    c=0
    for j in a:
        if j==i:
            c+=1
            pass
    if c==0:
        l.append(i)

print(*l)