n=int(input())
l=list(map(int,input().split()))
a=[]

for i in l:
    if i in a:
        continue
    if l.count(i)==i:
        print(i,end=" ")
        a.append(i)
if len(a)==0:
    print("-1")