n,m=map(int,input().split())
l=[]
for i in range(n):
    p=list(map(int,input().split()))
    l.append(p)
for i in (l):
    c=0
    c+=sum(i)
    print(c,end=" ")