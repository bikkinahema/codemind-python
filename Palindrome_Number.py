t=int(input())
for i in range(t):
    n=int(input())
    p=n
    l=0
    while n!=0:
        r=n%10
        n=n//10
        l=l*10+r
    if l==p:
        print("True")
    else:
        print("False")
        