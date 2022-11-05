n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i in k:
        continue
    k.append(i)
print(*k)
    