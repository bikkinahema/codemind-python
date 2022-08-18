n=int(input())
c=0
p=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
k=0
while n!=0:
    j=n//10
    r=n%10
    k=k*10+r
    n=j
for i in range(1,k+1):
    if k%i==0:
        p=p+1
if p==2 and c==2:
    print("circular prime")
elif (c==2 and p>2) or (p==2 and c>2):
    print("prime but not a circular prime")
else:
    print("not prime")
        