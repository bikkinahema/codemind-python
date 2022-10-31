n=int(input())
t=n
d=0
c=0
for i in range(1,(n//2)+1):
    if n%i==0:
        c+=1
if c==1:
    while n!=0:
        r=n%10
        k=0
        for j in range(1,(r//2)+1):
            if r%j==0:
                k+=1
        if k==1:
            d+=1
        n=n//10
p=str(t)
o=len(p)
if o==d:
    print("Mega Prime")
else:
    print("Not Mega Prime")
