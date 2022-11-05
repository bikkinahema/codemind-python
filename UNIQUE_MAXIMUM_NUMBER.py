n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i in k:
        continue
    if l.count(i)==1:
        k.append(i)
ma=0        
for i in k:
    if i>ma:
        ma=i
if len(k)==0:
    print("-1")
else:
    print(ma)
