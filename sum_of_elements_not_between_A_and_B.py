n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=len(l)
g=0
for i in range(0,k):
    if l[i]>=a and  l[i]<=b:
            continue
    else:
        g+=l[i]
        
print(g,end= ' ')