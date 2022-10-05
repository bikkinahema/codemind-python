n=int(input())
l=list(map(int,input().split()))
k=0
o=0
for i in range(0,n):
    if l[i]%2==0:
        k+=1
        if i%2==0:
            o+=1
if k==o:
    print("True")
else:
    print("False")
