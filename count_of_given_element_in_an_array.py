n=int(input())
l=list(map(int,input().split()))
a=int(input())
k=0
for i in range(0,n):
    if a==l[i]:
        k+=1
print(k)