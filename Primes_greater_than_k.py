n=int(input())
l=list(map(int,input().split()))
k=int(input())
d=0
for i in l:
    if i>=k:
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            d+=1
print(d)
        