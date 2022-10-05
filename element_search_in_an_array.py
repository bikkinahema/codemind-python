n=int(input())
l=list(map(int,input().split()))
a=int(input())
for i in range(0,n):
    if a==l[i]:
        print("True")
        break
else :
    print("False")