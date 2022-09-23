t=int(input())
for i in range(t):
    k=0
    l,r=map(int,input().split())
    for i in range(l,r+1):
        r=l%10
        if r==2 or r==3 or r==9:
            k+=1
        l+=1
    print(k)