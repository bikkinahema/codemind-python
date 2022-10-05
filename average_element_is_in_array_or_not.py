n=int(input())
l=list(map(int,input().split()))
t=0
for i in range(0,n):
   t+=l[i]
a=t//n
for j in range(0,n):
    if a==l[j]:
        print("True")
        break
else:
    print("False")
    