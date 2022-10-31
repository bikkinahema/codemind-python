n=int(input())
t=n
p=n
while True:
    c=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            c+=1
    if c==1:
        a=n
        break
    n+=1
while True:
    k=0
    for j in range(1,(t//2)+1):
        if t%j==0:
            k+=1
    if k==1:
        b=t
        break
    t-=1
x=a-p
y=p-b
if x>y:
    print(y)
else:
    print(x)