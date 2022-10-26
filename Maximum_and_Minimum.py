n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if l.count(i)==i:
        a.append(i)
if len(a)==0:
    print("-1")
else:
    k=max(a)
    f=min(a)
    print(f,k)