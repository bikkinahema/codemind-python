n=int(input())
l=list(map(int,input().split()))
k=l[0]
p=l.count(k)
for i in range(1,n):
    if p<l.count(l[i]):
        p=l.count(l[i])
for i in l:
    if l.count(i)==p:
        print(i)
        break
