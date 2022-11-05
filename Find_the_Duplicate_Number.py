n=int(input())
l=list(map(int,input().split()))
k=[]
p=[]
for i in l:
    if i in p:
        continue
    if l.count(i)>1:
        k.append(i)
    p.append(i)
print(*k)