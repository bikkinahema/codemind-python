n=int(input())
l=list(map(int,input().split()))
a=[]
k=0
for i in l:
    if i in a:
        continue
    else:
        a.append(i)
        if i%2==0:
            k+=i
print(k)
    