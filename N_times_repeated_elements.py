n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[ ]
for i in l:
    if i in a:
        continue
    if l.count(i) ==k:
        a.append(i)
if len(a)==0:
    print('-1')
else:
    print(*a)