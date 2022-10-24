n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
c=0
for i in a:
    for j in b:
        if j==i:
            if i not in l:
                c+=1
                l.append(i)
print(c)
            