n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
d=0
for i in l:
    if i>=a and i<=b:
        d+=i
else:
    print(d)
    
    