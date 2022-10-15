n=int(input())
l=list(map(int,input().split()))
d=0
t=0
for i in l:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        d+=i
        t+=1
ave=d/t
print("{:.2f}".format(ave))
        