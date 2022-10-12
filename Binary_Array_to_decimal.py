n=int(input())
l=list(map(int,input().split()))
k=len(l)
c=0
for i in range(0,k):
    n-=1
    c+=(2**n)*l[i]
print(c)
    