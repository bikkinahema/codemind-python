t=int(input())
for i in range(t):
    n=int(input())
    c=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            if i*i==n:
                c+=1
                print("True")
    if c==0:
        print("False")
            
    