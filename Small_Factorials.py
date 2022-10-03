t=int(input())
for i in range(t):
    n=int(input())
    f=1
    while n!=0:
        f*=n
        n=n-1
    print(f)