n=int(input())
l=list(map(int,input().split()))
t=0
for i in range(0,n):
    if i%2!=0:
        t+=int(l[i])
print(t)