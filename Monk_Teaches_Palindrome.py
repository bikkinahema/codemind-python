t=int(input())
for i in range(t):
    s=input()
    p=s[-1::-1]
    if s==p:
        k=len(s)
        a=str(k)
        if k%2==0:
            print("YES" , "EVEN")
        else:
            print("YES" , "ODD")
    elif s!=p:
        print("NO")
        