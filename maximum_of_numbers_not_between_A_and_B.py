n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
c=0
for i in range(0,n):
    if l[i]<a or l[i]>b:
        c+=1
        d.append(l[i])
if len(d)==0:
    print("-1")
else:
    print(max(d))