n=int(input())
l=list(map(int,input().split()))
k=0
for i in l:
    if i==0 or i==1:
        k+=1
if k==n:
    print("True")
else:
    print("False")