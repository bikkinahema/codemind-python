n1=int(input())
n2=int(input())
c=n1+n2
p=0
while True:
    c+=1
    p+=1
    k=0
    for i in range(1,c+1):
        if c%i==0:
            k+=1
    if k==2:
        print(p)
        break
    