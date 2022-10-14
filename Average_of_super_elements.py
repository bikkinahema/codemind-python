n=int(input())
l=list(map(int,input().split()))
a=[]
c=0
k=0
for i in l:
    if i in a:
        continue
    if l.count(i)==i:
        a.append(i)
        k+=i
        c+=1
if len(a)==0:
    print("-1")
else:
    print("{:.2f}".format(k/c))
        