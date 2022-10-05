n=int(input())
l=list(map(int,input().split()))
k=0
for i in range(0,n):
    if l[i]%2!=0:
        k=i
print(k)