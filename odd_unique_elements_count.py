n=int(input())
l=list(map(int,input().split()))
c=[]
a=0
for i in l:
    if i not in c:
        c.append(i)
        if i%2!=0:
            a+=1
print(a)
    