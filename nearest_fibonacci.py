n=int(input())
a=0
b=1
while b<n:
    c=a+b
    a=b
    b=c
k=n-a
p=b-n
if k<p:
    print(a)
elif p<k:
    print(b)
else:
    print(a,b,end=" ")