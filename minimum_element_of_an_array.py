n=int(input())
l=list(map(int,input().split()))
t=l[0]
for i in range(1,n):
    if t>l[i]:
        t=l[i]
print(t)
        