n=int(input())
l=list(map(int,input().split()))
t=0
for i in l:
    t+=i
av=t//n
k=0
for i in l:
    if i<=av:
        k+=1
print(k)
    