n=int(input())
l=list(map(int,input().split()))
c=0
a=[]
for i in l:
    if i in a:
        continue
    if l.count(i)==i:
        a.append(i)
        c+=1
print(c)
