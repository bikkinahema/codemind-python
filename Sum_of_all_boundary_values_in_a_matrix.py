n,m=map(int,input().split())
l=[]
for i in range(n):
    p=list(map(int,input().split()))
    l.append(p)
s=0
s+=sum(l[0])
s+=sum(l[-1])
for i in range(n):
    s+=l[i][0]
for i in range(n):
    s+=l[i][m-1]
print(s-l[0][0]-l[0][-1]-l[-1][-1]-l[n-1][0])