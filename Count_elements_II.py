n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
s=0
for i in a:
    c=0
    for j in b:
        if j==i:
            c+=1
            pass
    if c==0:
        if i not in l:
            l.append(i)
            s+=1
for i in b:
    c=0
    for j in a:
        if j==i:
            c+=1
            pass
    if c==0:
        if i not in l:
            l.append(i)
            s+=1

print(s)