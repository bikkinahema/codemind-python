n=int(input())
while n>9:
    l=0
    while n!=0:
        r=n%10
        n=n//10
        l+=r*r
    n=l
if n==1 or n==7:
    print("True")
else:
    print("False")
    