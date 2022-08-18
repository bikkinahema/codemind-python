n=int(input())
t=n
k=0
while n!=0:
    c=n//10
    r=n%10
    n=c
    f=1
    while r!=0:
        f=f*r
        r=r-1
    k=k+f
if k==t:
    print("The number {} is a strong number".format(t))
else:
    print("The number {} is not a strong number".format(t))
        