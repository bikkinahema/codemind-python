a,b=map(int,input().split())
l=1
t=2
while True:
    if a%t==0 and b%t==0:
        a=a//t
        b=b//t
        l=l*t
    else:
        t+=1
        if a<t or b<t:
            break
print(l*a*b)