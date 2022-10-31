n=int(input())
p=n
t=n
while True:
    rev=0
    while n!=0:
        r=n%10
        n=n//10
        rev=rev*10+r
    p+=rev
    k=p
    rev1=0
    while k!=0:
        r1=k%10
        k=k//10
        rev1=rev1*10+r1
    if rev1==p:
        print(p)
        break
    n=p
