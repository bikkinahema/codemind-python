n=int(input())
l=list(map(int,input().split()))
k=[]
p=[]
for i in range(0,n):
    if i%2==0:
        k.append(l[i])
    else:
        p.append(l[i])
s=0
d=0
for j in k:
    s+=j
for t in p:
    d+=t
if ((d-s)==0):
    print("YES")
else:
    print("NO")

    