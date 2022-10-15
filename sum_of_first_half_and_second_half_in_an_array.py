n=int(input())
l=list(map(int,input().split()))
k=n/2
p=int(k)
x=0
y=0
for i in range(0,p):
    x+=l[i]
for i in range(p,n):
    y+=l[i]

print(x)
print(y)
    