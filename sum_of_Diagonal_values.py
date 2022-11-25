n,m=map(int,input().split())
l=[]
for i in range(n):
    p=list(map(int,input().split()))
    l.append(p)
s=0
for i in range(n):
    s+=l[i][i]
    s+=l[i][-i-1]
if n%2:
    s-=l[n//2][n//2]
print(s)