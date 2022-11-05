n=int(input())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
k=[]
for i in range(0,n):
    c=l[i]+p[i]
    k.append(c)
print(*k)
    