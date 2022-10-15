n=int(input())
l=list(map(int,input().split()))
c=0
k=int(input())
for i in l:
    c+=i
    if i==k:
        break
print(c)
        