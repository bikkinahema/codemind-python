n=int(input())
e=0
o=0
while n!=0:
    r=n%10
    if n%2==0:
        e+=1
    else:
        o+=1
    n=n//10
if e==0 and o>1:
    print("Odd")
elif o==0 and e>1:
    print("Even")
else:
    print("Mixed")