n,m=map(int,input().split())
l=[]
for i in range(n):
    p=list(map(int,input().split()))
    l.append(p)
a=[]
for i in l:
    c=0
    c+=sum(i)
    a.append(c)
print(max(a))