a=int(input())
b=int(input())
for i in range(a,b+1):
    rev=0
    x=i
    while i!=0:
        r=i%10
        i=i//10
        rev=rev*10+r
    if rev==x:
        print(x,end=' ')
        