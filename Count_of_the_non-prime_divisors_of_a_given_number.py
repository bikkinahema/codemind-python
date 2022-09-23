n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        k=0
        for j in range(1,i+1):
            if i%j==0:
                k+=1
        if k>2 or k==1:
            c+=1
print(c)
            
    