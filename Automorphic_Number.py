n=int(input())
t=str(n)
k=len(t)
s=n*n
l=0
while s!=0:
    r=s%10
    l=l*10+r
    a=str(l)
    b=a[::-1]
    c=len(b)
    if k==c:
        d=int(b)
        if d==n:
            print("Automorphic Number")
            break
    s=s//10
    if k<c:
        print("Not an Automorphic Number")
        break
    